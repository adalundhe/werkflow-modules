from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_pod_identity_association_summary import EKSPodIdentityAssociationSummary


class EKSListPodIdentityAssociationsResponse(BaseModel):
    associations: list[EKSPodIdentityAssociationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
