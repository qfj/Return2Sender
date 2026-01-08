import json
import redis
from datetime import datetime, timezone
import os

redis_host = os.getenv("REDIS_HOST", "redis")  # point to Redis container
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

good_event = {
    "service": "pricing-engine",
    "severity": "ERROR",
    "message": "Division by zero",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "trace_id": "abc-123",
}

bad_event = {
    "service": "risk-engine",
    "message": "Missing fields",
}

r.xadd("errors:in", {"payload": json.dumps(good_event)})
r.xadd("errors:in", {"payload": json.dumps(bad_event)})

print("sent good + bad")
