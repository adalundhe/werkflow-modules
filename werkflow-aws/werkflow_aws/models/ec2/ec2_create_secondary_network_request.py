from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateSecondaryNetworkRequest(BaseModel):
    Ipv4CidrBlock: StrictStr
    NetworkType: Literal['rdma']
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
