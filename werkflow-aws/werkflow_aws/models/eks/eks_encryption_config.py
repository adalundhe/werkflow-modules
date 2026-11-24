from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_provider import EKSProvider


class EKSEncryptionConfig(BaseModel):
    resources: list[StrictStr] | None = None
    provider: EKSProvider | None = None
