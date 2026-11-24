from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_update_model import EKSUpdateModel


class EKSCancelUpdateResponse(BaseModel):
    update: EKSUpdateModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
