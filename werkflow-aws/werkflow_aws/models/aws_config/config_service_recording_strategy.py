from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceRecordingStrategy(BaseModel):
    useOnly: StrictStr | None = None
