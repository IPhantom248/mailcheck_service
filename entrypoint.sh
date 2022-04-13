#!/bin/bash

celery -A main worker -l INFO &
celery -A main beat -l INFO &
exec "$@"