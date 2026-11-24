from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class LambdaInvokeResponseStreamUpdate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Payload: StrictBytes | Any | None = None
