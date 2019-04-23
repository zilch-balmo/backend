#!/bin/bash -e

if [ "$1" = "uwsgi" ] || [ "$1" = "server" ]; then
    cat > logging.conf <<EOF
[uwsgi]
logger = stdio
logger = ignore file:/dev/null
log-route = ignore /api/health
EOF

    exec uwsgi \
	 --http 0.0.0.0:80 \
	 --http-uid nobody \
	 --http-gid nobody \
	 --http-timeout 6 \
	 --http-workers 2 \
	 --module backend.wsgi:app \
	 --ini logging.conf
elif [ "$1" = "shell" ]; then
    exec /bin/bash
else
    exec /bin/bash -c "$*"
fi
