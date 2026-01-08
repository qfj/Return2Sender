import json
import redis
from pydantic import ValidationError
from schemas.error import ErrorEvent

r = redis.Redis(host="redis", port=6379, decode_responses=True)

last_id = "0-0"

print("validator running...")

while True:
    results = r.xread({"errors:in": last_id}, block=0)

    for stream, messages in results:
        for msg_id, fields in messages:
            last_id = msg_id
            raw = fields.get("payload")

            try:
                payload = json.loads(raw)
                ErrorEvent(**payload)

                r.xadd("errors:valid", {"payload": raw})
                print("VALID:", payload)

            except (json.JSONDecodeError, ValidationError) as e:
                r.xadd(
                    "errors:returned",
                    {
                        "original": raw,
                        "error": str(e),
                    },
                )
                print("RETURNED:", raw)
