from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2GetCapacityManagerAttributesRequest(BaseModel):
    DryRun: StrictBool | None = None
