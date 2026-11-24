from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image_usage_report import EC2ImageUsageReport


class EC2DescribeImageUsageReportsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ImageUsageReports: list[EC2ImageUsageReport] | None = None
    ResponseMetadata: dict[str, Any] | None = None
