from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_service_detail import EC2ServiceDetail


class EC2DescribeVpcEndpointServicesResponse(BaseModel):
    ServiceNames: list[StrictStr] | None = None
    ServiceDetails: list[EC2ServiceDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
