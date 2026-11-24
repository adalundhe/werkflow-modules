from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_import_snapshot_task import EC2ImportSnapshotTask


class EC2DescribeImportSnapshotTasksResponse(BaseModel):
    ImportSnapshotTasks: list[EC2ImportSnapshotTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
