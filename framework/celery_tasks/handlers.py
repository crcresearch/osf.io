# -*- coding: utf-8 -*-
import logging
import threading
import functools

from celery import group
from flask import _app_ctx_stack as context_stack

from api.base.api_globals import api_globals
from website import settings
f = open('celery_log', 'a')
f.write("hello_handler\n")
f.close()


_local = threading.local()
logger = logging.getLogger(__name__)


def queue():
    f = open('celery_log', 'a')
    f.write("hello_queue_task\n")
    f.close()
    if not hasattr(_local, 'queue'):
        _local.queue = []
    return _local.queue


def celery_before_request():
    f = open('celery_log', 'a')
    f.write("hello_before_task\n")
    f.close()
    _local.queue = []


def celery_after_request(response, base_status_code_error=500):
    f = open('celery_log', 'a')
    f.write("hello_after_task\n")
    f.close()
    if response.status_code >= base_status_code_error:
        _local.queue = []
    return response


def celery_teardown_request(error=None):
    f = open('celery_log', 'a')
    f.write("hello_teardown_task\n")
    f.close()
    if error is not None:
        _local.queue = []
        return
    if queue():
        if settings.USE_CELERY:
            group(queue()).apply_async()
        else:
            for task in queue():
                task.apply()


def enqueue_task(signature):
    """If working in a request context, push task signature to thread-local
    queue to run after request is complete; else run signature immediately.
    :param signature: Celery task signature
    """
    f = open('celery_log', 'a')
    f.write("hello_enqueue_task\n")
    f.close()
    if (
        context_stack.top is None and
        getattr(api_globals, 'request', None) is None
    ):  # Not in a request context
        signature()
    else:
        if signature not in queue():
            queue().append(signature)


def queued_task(task):
    """Decorator that adds the wrapped task to the queue on ``g`` if Celery is
    enabled, else runs the task synchronously. Can only be applied to Celery
    tasks; should be used for all tasks fired within a request context that
    may write to the database to avoid race conditions.
    """
    @functools.wraps(task)
    def wrapped(*args, **kwargs):
        signature = task.si(*args, **kwargs)
        enqueue_task(signature)
    return wrapped


handlers = {
    'before_request': celery_before_request,
    'after_request': celery_after_request,
    'teardown_request': celery_teardown_request,
}
