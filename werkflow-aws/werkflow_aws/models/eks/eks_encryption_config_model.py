from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_provider_model import EKSProviderModel


class EKSEncryptionConfigModel(BaseModel):
    resources: list[StrictStr] | None = None
    provider: EKSProviderModel | None = None
