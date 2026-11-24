from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_pod_identity_association import EKSPodIdentityAssociation


class EKSDescribePodIdentityAssociationResponse(BaseModel):
    association: EKSPodIdentityAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
