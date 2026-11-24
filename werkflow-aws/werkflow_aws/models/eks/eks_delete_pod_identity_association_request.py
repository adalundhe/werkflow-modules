from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeletePodIdentityAssociationRequest(BaseModel):
    clusterName: StrictStr
    associationId: StrictStr
