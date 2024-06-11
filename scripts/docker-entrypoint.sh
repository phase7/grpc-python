#!/bin/sh
set -ex

case $1 in
    server)
        echo "initilizin database..."
        exec python -u init_db.py
        # Shift arguments to the left so $1 now refers to the first argument after "run_publisher"
        shift
        if [ $# -eq 0 ]; then
          python -u server.py
        else
          python -u server.py "$@"
        fi
        ;;
    client)
        echo "init benchmarking..."
        shift
        if [ $# -eq 0 ]; then
          python -u client.py --iterations 20
        else
          python -u client.py "$@"
        fi
        ;;
    *)
        echo "Unfamiliar command: $1. executing the command..."
        exec "$@"
        ;;
esac