from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_replace_root_volume_task import EC2ReplaceRootVolumeTask


class EC2DescribeReplaceRootVolumeTasksResponse(BaseModel):
    ReplaceRootVolumeTasks: list[EC2ReplaceRootVolumeTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
