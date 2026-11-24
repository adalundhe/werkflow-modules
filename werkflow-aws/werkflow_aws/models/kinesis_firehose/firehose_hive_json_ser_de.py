from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseHiveJsonSerDe(BaseModel):
    TimestampFormats: list[StrictStr] | None = None
