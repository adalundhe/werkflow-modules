from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class BedrockRuntimePayloadPart(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    bytes: StrictBytes | Any | None = None
