from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_vpc_encryption_control_configuration import EC2VpcEncryptionControlConfiguration


class EC2CreateVpcRequest(BaseModel):
    CidrBlock: StrictStr | None = None
    Ipv6Pool: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    Ipv4IpamPoolId: StrictStr | None = None
    Ipv4NetmaskLength: StrictInt | None = None
    Ipv6IpamPoolId: StrictStr | None = None
    Ipv6NetmaskLength: StrictInt | None = None
    Ipv6CidrBlockNetworkBorderGroup: StrictStr | None = None
    VpcEncryptionControl: EC2VpcEncryptionControlConfiguration | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    InstanceTenancy: Literal['default', 'dedicated', 'host'] | None = None
    AmazonProvidedIpv6CidrBlock: StrictBool | None = None
