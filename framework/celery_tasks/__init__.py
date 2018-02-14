# -*- coding: utf-8 -*-
"""Asynchronous task queue module."""
from celery import Celery, signals
from celery.utils.log import get_task_logger

from raven import Client
from raven.contrib.celery import register_signal

from website.settings import SENTRY_DSN, VERSION, CeleryConfig

f = open('celery_log', 'a') 
f.write("hello1\n")
f.close()

#@signals.setup_logging.connect
#def setup_celery_logging(**kwargs):
#    pass

f = open('celery_log', 'a') 
f.write("hello22\n")
f.close()

app = Celery()
#app.config_from_object(CeleryConfig)
#app.log.setup()
app.config_from_object(CeleryConfig, namespace='CELERY')

f = open('celery_log', 'a') 
f.write("hello3\n")
f.close()

if SENTRY_DSN:
    client = Client(SENTRY_DSN, release=VERSION, tags={'App': 'celery'})
    register_signal(client)

if CeleryConfig.broker_use_ssl:
    app.setup_security()

f = open('celery_log', 'a') 
f.write("hello4\n")
f.close()

@app.task
def error_handler(task_id, task_name):
    """logs detailed message about tasks that raise exceptions

    :param task_id: TaskID of the failed task
    :param task_name: name of task that failed
    """
    f = open('celery_log', 'a') 
    f.write("hello5\n")
    f.close()
    # get the current logger
    logger = get_task_logger(__name__)
    # query the broker for the AsyncResult
    result = app.AsyncResult(task_id)
    excep = result.get(propagate=False)
    # log detailed error mesage in error log
    logger.error('#####FAILURE LOG BEGIN#####\n'
                'Task {0} raised exception: {0}\n\{0}\n'
                '#####FAILURE LOG STOP#####'.format(task_name, excep, result.traceback))
