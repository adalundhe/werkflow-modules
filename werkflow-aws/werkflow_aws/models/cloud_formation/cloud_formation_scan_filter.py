from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationScanFilter(BaseModel):
    Types: list[StrictStr] | None = None
