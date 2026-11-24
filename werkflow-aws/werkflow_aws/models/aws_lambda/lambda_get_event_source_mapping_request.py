from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetEventSourceMappingRequest(BaseModel):
    UUID: StrictStr
