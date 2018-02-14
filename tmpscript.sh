#!/bin/bash

for reqs_file in \
        ./requirements.txt \
        ./requirements/release.txt \
        ./addons/*/requirements.txt \
; do \
        pip install --no-cache-dir -c ./requirements/constraints.txt -r "$reqs_file" \
; done \
&& (pip uninstall uritemplate.py --yes || true) \
&& pip install --no-cache-dir uritemplate.py==0.3.0 \
# Fix: https://github.com/CenterForOpenScience/osf.io/pull/6783
&& python -m compileall /usr/local/lib/python2.7 || true
