from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceConfigurationRecorderFilter(BaseModel):
    filterName: Literal['recordingScope'] | None = None
    filterValue: list[StrictStr] | None = None
