from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_snapshot_task_detail import EC2SnapshotTaskDetail
from .ec2_tag_model import EC2TagModel


class EC2ImportSnapshotTask(BaseModel):
    Description: StrictStr | None = None
    ImportTaskId: StrictStr | None = None
    SnapshotTaskDetail: EC2SnapshotTaskDetail | None = None
    Tags: list[EC2TagModel] | None = None
