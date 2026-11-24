from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_connect_endpoint_public_dns_names import EC2InstanceConnectEndpointPublicDnsNames
from .ec2_tag_model import EC2TagModel


class Ec2InstanceConnectEndpoint(BaseModel):
    OwnerId: StrictStr | None = None
    InstanceConnectEndpointId: StrictStr | None = None
    InstanceConnectEndpointArn: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    DnsName: StrictStr | None = None
    FipsDnsName: StrictStr | None = None
    NetworkInterfaceIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    SubnetId: StrictStr | None = None
    PreserveClientIp: StrictBool | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: list[EC2TagModel] | None = None
    IpAddressType: StrictStr | None = None
    PublicDnsNames: EC2InstanceConnectEndpointPublicDnsNames | None = None
    AvailabilityZoneId: StrictStr | None = None
