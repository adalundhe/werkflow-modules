from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTUpdateEncryptionConfigurationRequest(BaseModel):
    encryptionType: Literal['CUSTOMER_MANAGED_KMS_KEY', 'AWS_OWNED_KMS_KEY']
    kmsKeyArn: StrictStr | None = None
    kmsAccessRoleArn: StrictStr | None = None
