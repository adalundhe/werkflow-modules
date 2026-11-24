from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_dns_entry import EC2DnsEntry
from .ec2_tag_model import EC2TagModel


class EC2VpcEndpointAssociation(BaseModel):
    Id: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
    ServiceNetworkArn: StrictStr | None = None
    ServiceNetworkName: StrictStr | None = None
    AssociatedResourceAccessibility: StrictStr | None = None
    FailureReason: StrictStr | None = None
    FailureCode: StrictStr | None = None
    DnsEntry: EC2DnsEntry | None = None
    PrivateDnsEntry: EC2DnsEntry | None = None
    AssociatedResourceArn: StrictStr | None = None
    ResourceConfigurationGroupArn: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
