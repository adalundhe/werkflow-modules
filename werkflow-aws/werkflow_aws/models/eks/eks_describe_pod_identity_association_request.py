from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribePodIdentityAssociationRequest(BaseModel):
    clusterName: StrictStr
    associationId: StrictStr
