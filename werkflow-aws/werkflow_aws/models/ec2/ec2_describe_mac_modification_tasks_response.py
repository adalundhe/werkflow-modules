from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_mac_modification_task import EC2MacModificationTask


class EC2DescribeMacModificationTasksResponse(BaseModel):
    MacModificationTasks: list[EC2MacModificationTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
