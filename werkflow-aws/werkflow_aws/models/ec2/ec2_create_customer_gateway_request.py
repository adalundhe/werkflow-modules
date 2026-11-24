from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCustomerGatewayRequest(BaseModel):
    Type: Literal['ipsec.1']
    BgpAsn: StrictInt | None = None
    PublicIp: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DeviceName: StrictStr | None = None
    IpAddress: StrictStr | None = None
    BgpAsnExtended: StrictInt | None = None
    DryRun: StrictBool | None = None
