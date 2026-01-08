from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Literal


class ErrorEvent(BaseModel):
    service: str = Field(..., min_length=1)
    severity: Literal["INFO", "WARN", "ERROR", "CRITICAL"]
    message: str = Field(..., min_length=1)
    timestamp: datetime
    trace_id: str
