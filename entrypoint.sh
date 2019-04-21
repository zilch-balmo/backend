#!/bin/bash -e

if [ "$1" = "uwsgi" ] || [ "$1" = "server" ]; then
    exec uwsgi \
	 --http-uid nobody \
	 --http-gid nobody \
	 --http 0.0.0.0:80 \
	 --module backend.wsgi:app
elif [ "$1" = "gunicorn" ]; then
    exec gunicorn \
	 --access-logfile - \
	 --bind 0.0.0.0:80 \
	 --log-level DEBUG \
	 --user nobody \
	 --group nobody \
	 --workers 4 \
	 --worker-class gevent \
	 --timeout 6 \
	 --graceful-timeout 6 \
	 backend.wsgi:app
elif [ "$1" = "shell" ]; then
    exec /bin/bash
else
    exec /bin/bash -c "$*"
fi
