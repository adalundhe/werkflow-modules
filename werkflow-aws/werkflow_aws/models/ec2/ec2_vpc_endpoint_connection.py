from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_dns_entry import EC2DnsEntry
from .ec2_payer_responsibility_entry import EC2PayerResponsibilityEntry
from .ec2_tag_model import EC2TagModel


class EC2VpcEndpointConnection(BaseModel):
    ServiceId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
    VpcEndpointOwner: StrictStr | None = None
    VpcEndpointState: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    DnsEntries: list[EC2DnsEntry] | None = None
    NetworkLoadBalancerArns: list[StrictStr] | None = None
    GatewayLoadBalancerArns: list[StrictStr] | None = None
    IpAddressType: StrictStr | None = None
    VpcEndpointConnectionId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    VpcEndpointRegion: StrictStr | None = None
    PayerResponsibilities: list[EC2PayerResponsibilityEntry] | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayAttachmentOwner: StrictStr | None = None
