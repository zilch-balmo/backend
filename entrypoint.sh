#!/bin/bash -e

if [ "$1" = "uwsgi" ]; then
    exec uwsgi \
	 --http 0.0.0.0:80 \
	 --http-uid nobody \
	 --http-gid nobody \
	 --http-workers 2 \
	 --module backend.wsgi:app
elif [ "$1" = "gunicorn" ] || [ "$1" = "server" ]; then
    exec gunicorn \
	 --access-logfile - \
	 --bind 0.0.0.0:80 \
	 --log-level DEBUG \
	 --user nobody \
	 --group nobody \
	 --workers 2 \
	 --worker-class gevent \
	 --timeout 10 \
	 --graceful-timeout 10 \
	 backend.wsgi:app
elif [ "$1" = "shell" ]; then
    exec /bin/bash
else
    exec /bin/bash -c "$*"
fi
