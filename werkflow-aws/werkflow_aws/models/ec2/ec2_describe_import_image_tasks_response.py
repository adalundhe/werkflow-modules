from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_import_image_task import EC2ImportImageTask


class EC2DescribeImportImageTasksResponse(BaseModel):
    ImportImageTasks: list[EC2ImportImageTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
