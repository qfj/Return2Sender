#!/bin/bash
docker-compose up -d --build
echo "Validator and Redis running."
echo "Watch validator logs:"
echo "  docker logs -f return2sender_validator_1"
echo "Send messages interactively:"
echo "  docker exec -it return2sender_validator_1 python3 /app/producer/producer.py"