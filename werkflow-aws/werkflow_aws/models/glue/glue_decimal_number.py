from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt


class GlueDecimalNumber(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    UnscaledValue: StrictBytes | Any | None = None
    Scale: StrictInt | None = None
