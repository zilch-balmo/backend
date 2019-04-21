#!/bin/bash -e

#	 --worker-class gevent \
#	 --timeout 6 \
#	 --graceful-timeout 6 \

if [ "$1" = "server" ]; then
    exec gunicorn \
	 --access-logfile - \
	 --bind 0.0.0.0:80 \
	 --user nobody \
	 --group nobody \
	 --workers 4 \
	 "backend.wsgi:app"
elif [ "$1" = "shell" ]; then
    exec /bin/bash
else
    exec /bin/bash -c "$*"
fi
