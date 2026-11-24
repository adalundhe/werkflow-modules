from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_trunk_interface_association import EC2TrunkInterfaceAssociation


class EC2AssociateTrunkInterfaceResponse(BaseModel):
    InterfaceAssociation: EC2TrunkInterfaceAssociation | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
