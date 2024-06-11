#!/bin/sh
set -ex

case $1 in
    server)
        # Shift arguments to the left so $1 now refers to the first argument after "run_publisher"
        shift
        if [ $# -eq 0 ]; then
          python -u publisher.py --num-of-runs $NUM_OF_RUNS --pubsub
        else
          python -u publisher.py "$@"
        fi
        ;;
    client)
        echo "Starting the subscriber..."
        uvicorn subscriber:app --host 0.0.0.0 --port 8000
        ;;
    *)
        echo "Unfamiliar command: $1. executing the command..."
        exec "$@"
        ;;
esac