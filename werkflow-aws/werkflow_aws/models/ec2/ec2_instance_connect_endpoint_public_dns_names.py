from __future__ import annotations
from pydantic import BaseModel
from .ec2_instance_connect_endpoint_dns_names import EC2InstanceConnectEndpointDnsNames


class EC2InstanceConnectEndpointPublicDnsNames(BaseModel):
    Ipv4: EC2InstanceConnectEndpointDnsNames | None = None
    Dualstack: EC2InstanceConnectEndpointDnsNames | None = None
