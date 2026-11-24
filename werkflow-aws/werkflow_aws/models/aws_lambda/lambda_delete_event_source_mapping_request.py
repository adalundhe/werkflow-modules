from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteEventSourceMappingRequest(BaseModel):
    UUID: StrictStr
