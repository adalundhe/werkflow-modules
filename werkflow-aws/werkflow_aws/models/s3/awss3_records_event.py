from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class AWSS3RecordsEvent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Payload: StrictBytes | Any | None = None
