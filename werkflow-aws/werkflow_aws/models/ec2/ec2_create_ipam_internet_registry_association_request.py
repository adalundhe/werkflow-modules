from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamInternetRegistryAssociationRequest(BaseModel):
    IpamId: StrictStr
    Rir: Literal['ripe', 'apnic', 'arin', 'lacnic', 'nicbr']
    OrganizationHandle: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
