from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image_usage_report_entry import EC2ImageUsageReportEntry


class EC2DescribeImageUsageReportEntriesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ImageUsageReportEntries: list[EC2ImageUsageReportEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
