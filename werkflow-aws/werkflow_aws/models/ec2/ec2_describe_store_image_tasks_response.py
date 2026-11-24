from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_store_image_task_result import EC2StoreImageTaskResult


class EC2DescribeStoreImageTasksResponse(BaseModel):
    StoreImageTaskResults: list[EC2StoreImageTaskResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
