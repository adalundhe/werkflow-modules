from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_encryption_config_model import EKSEncryptionConfigModel


class EKSAssociateEncryptionConfigRequest(BaseModel):
    clusterName: StrictStr
    encryptionConfig: list[EKSEncryptionConfigModel]
    clientRequestToken: StrictStr | None = None
