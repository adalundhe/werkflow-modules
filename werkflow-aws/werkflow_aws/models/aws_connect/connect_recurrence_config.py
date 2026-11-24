from __future__ import annotations
from pydantic import BaseModel
from .connect_recurrence_pattern import ConnectRecurrencePattern


class ConnectRecurrenceConfig(BaseModel):
    RecurrencePattern: ConnectRecurrencePattern | None = None
