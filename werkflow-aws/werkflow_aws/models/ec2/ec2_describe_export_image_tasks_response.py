from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_export_image_task import EC2ExportImageTask


class EC2DescribeExportImageTasksResponse(BaseModel):
    ExportImageTasks: list[EC2ExportImageTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
