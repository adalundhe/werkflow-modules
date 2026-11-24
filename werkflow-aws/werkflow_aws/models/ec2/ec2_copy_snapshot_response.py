from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2CopySnapshotResponse(BaseModel):
    Tags: list[EC2TagModel] | None = None
    SnapshotId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
