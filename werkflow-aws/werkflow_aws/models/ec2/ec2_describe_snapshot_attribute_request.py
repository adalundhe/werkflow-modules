from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeSnapshotAttributeRequest(BaseModel):
    Attribute: Literal['productCodes', 'createVolumePermission']
    SnapshotId: StrictStr
    DryRun: StrictBool | None = None
