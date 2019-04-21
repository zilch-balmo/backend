#!/bin/bash -e

if [ "$1" = "uwsgi" ] || [ "$1" = "server" ]; then
    exec uwsgi \
	 --http 0.0.0.0:80 \
	 --http-uid nobody \
	 --http-gid nobody \
	 --http-timeout 6 \
	 --http-workers 2 \
	 --module backend.wsgi:app
elif [ "$1" = "shell" ]; then
    exec /bin/bash
else
    exec /bin/bash -c "$*"
fi
