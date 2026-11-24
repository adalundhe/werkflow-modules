from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2CustomerGateway(BaseModel):
    CertificateArn: StrictStr | None = None
    DeviceName: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    BgpAsnExtended: StrictStr | None = None
    CustomerGatewayId: StrictStr | None = None
    State: StrictStr | None = None
    Type: StrictStr | None = None
    IpAddress: StrictStr | None = None
    BgpAsn: StrictStr | None = None
