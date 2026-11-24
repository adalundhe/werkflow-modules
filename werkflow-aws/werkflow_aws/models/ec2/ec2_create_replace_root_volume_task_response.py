from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_replace_root_volume_task import EC2ReplaceRootVolumeTask


class EC2CreateReplaceRootVolumeTaskResponse(BaseModel):
    ReplaceRootVolumeTask: EC2ReplaceRootVolumeTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
