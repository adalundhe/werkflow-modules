from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_update_model import EKSUpdateModel


class EKSAssociateIdentityProviderConfigResponse(BaseModel):
    update: EKSUpdateModel | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
