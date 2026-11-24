from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_associated_access_policy import EKSAssociatedAccessPolicy


class EKSListAssociatedAccessPoliciesResponse(BaseModel):
    clusterName: StrictStr | None = None
    principalArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    associatedAccessPolicies: list[EKSAssociatedAccessPolicy] | None = None
    ResponseMetadata: dict[str, Any] | None = None
