from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_associated_access_policy import EKSAssociatedAccessPolicy


class EKSAssociateAccessPolicyResponse(BaseModel):
    clusterName: StrictStr | None = None
    principalArn: StrictStr | None = None
    associatedAccessPolicy: EKSAssociatedAccessPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
