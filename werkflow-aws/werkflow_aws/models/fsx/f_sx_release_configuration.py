from __future__ import annotations
from pydantic import BaseModel
from .f_sx_duration_since_last_access import FSxDurationSinceLastAccess


class FSxReleaseConfiguration(BaseModel):
    DurationSinceLastAccess: FSxDurationSinceLastAccess | None = None
