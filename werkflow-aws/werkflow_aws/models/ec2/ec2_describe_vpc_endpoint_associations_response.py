from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_endpoint_association import EC2VpcEndpointAssociation


class EC2DescribeVpcEndpointAssociationsResponse(BaseModel):
    VpcEndpointAssociations: list[EC2VpcEndpointAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
