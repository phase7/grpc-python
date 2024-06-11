#!/bin/sh
set -ex

case $1 in
    server)
        echo "initilizing database..."
        python -u init_db.py
        # Shift arguments to the left so $1 now refers to the first argument after "run_publisher"
        shift
        python src/server.py
        ;;
    client)
        echo "init benchmarking..."
        shift
        if [ $# -eq 0 ]; then
          python -u src/client.py --iterations 20
        else
          python -u src/client.py "$@"
        fi
        ;;
    *)
        echo "Unfamiliar command: $1. executing the command..."
        exec "$@"
        ;;
esac