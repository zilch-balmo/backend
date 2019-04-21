#!/bin/bash -e


if [ "$1" = "server" ]; then
    exec uwsgi \
	 --uid nobody \
	 --gid nobody \
	 --http 0.0.0.0:8080 \
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
