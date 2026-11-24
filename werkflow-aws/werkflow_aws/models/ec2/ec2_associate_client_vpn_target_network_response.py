from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_association_status import EC2AssociationStatus


class EC2AssociateClientVpnTargetNetworkResponse(BaseModel):
    AssociationId: StrictStr | None = None
    Status: EC2AssociationStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
