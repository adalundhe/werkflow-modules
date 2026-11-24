from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_dns_entry import EC2DnsEntry
from .ec2_dns_options import EC2DnsOptions
from .ec2_last_error import EC2LastError
from .ec2_payer_responsibility_entry import EC2PayerResponsibilityEntry
from .ec2_security_group_identifier import EC2SecurityGroupIdentifier
from .ec2_subnet_ip_prefixes import EC2SubnetIpPrefixes
from .ec2_tag_model import EC2TagModel


class EC2VpcEndpoint(BaseModel):
    VpcEndpointId: StrictStr | None = None
    VpcEndpointType: StrictStr | None = None
    VpcId: StrictStr | None = None
    ServiceName: StrictStr | None = None
    State: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    RouteTableIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    Groups: list[EC2SecurityGroupIdentifier] | None = None
    IpAddressType: StrictStr | None = None
    DnsOptions: EC2DnsOptions | None = None
    PrivateDnsEnabled: StrictBool | None = None
    RequesterManaged: StrictBool | None = None
    NetworkInterfaceIds: list[StrictStr] | None = None
    DnsEntries: list[EC2DnsEntry] | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    OwnerId: StrictStr | None = None
    LastError: EC2LastError | None = None
    Ipv4Prefixes: list[EC2SubnetIpPrefixes] | None = None
    Ipv6Prefixes: list[EC2SubnetIpPrefixes] | None = None
    FailureReason: StrictStr | None = None
    ServiceNetworkArn: StrictStr | None = None
    ResourceConfigurationArn: StrictStr | None = None
    ServiceRegion: StrictStr | None = None
    PayerResponsibilities: list[EC2PayerResponsibilityEntry] | None = None
