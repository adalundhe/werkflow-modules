from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_cidr_authorization_context import EC2CidrAuthorizationContext
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2ProvisionByoipCidrRequest(BaseModel):
    Cidr: StrictStr
    CidrAuthorizationContext: EC2CidrAuthorizationContext | None = None
    PubliclyAdvertisable: StrictBool | None = None
    Description: StrictStr | None = None
    DryRun: StrictBool | None = None
    PoolTagSpecifications: list[EC2TagSpecificationModel] | None = None
    MultiRegion: StrictBool | None = None
    NetworkBorderGroup: StrictStr | None = None
