from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_manager_data_export_response import EC2CapacityManagerDataExportResponse


class EC2DescribeCapacityManagerDataExportsResponse(BaseModel):
    CapacityManagerDataExports: list[EC2CapacityManagerDataExportResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
