from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_service_configuration import EC2ServiceConfiguration


class EC2DescribeVpcEndpointServiceConfigurationsResponse(BaseModel):
    ServiceConfigurations: list[EC2ServiceConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
