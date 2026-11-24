from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TrunkInterfaceAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    BranchInterfaceId: StrictStr | None = None
    TrunkInterfaceId: StrictStr | None = None
    InterfaceProtocol: StrictStr | None = None
    VlanId: StrictInt | None = None
    GreKey: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
