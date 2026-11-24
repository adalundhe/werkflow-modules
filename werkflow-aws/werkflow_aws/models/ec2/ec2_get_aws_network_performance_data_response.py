from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_data_response import EC2DataResponse


class EC2GetAwsNetworkPerformanceDataResponse(BaseModel):
    DataResponses: list[EC2DataResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
