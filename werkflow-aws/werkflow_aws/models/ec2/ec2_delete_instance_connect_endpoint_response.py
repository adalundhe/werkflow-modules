from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_connect_endpoint import Ec2InstanceConnectEndpoint


class EC2DeleteInstanceConnectEndpointResponse(BaseModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
