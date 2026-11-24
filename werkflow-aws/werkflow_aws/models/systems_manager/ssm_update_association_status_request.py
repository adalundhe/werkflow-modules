from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_association_status import SSMAssociationStatus


class SSMUpdateAssociationStatusRequest(BaseModel):
    Name: StrictStr
    InstanceId: StrictStr
    AssociationStatus: SSMAssociationStatus
