from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_vpc_cidr_block_state import EC2VpcCidrBlockState


class EC2VpcCidrBlockAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    CidrBlockState: EC2VpcCidrBlockState | None = None
