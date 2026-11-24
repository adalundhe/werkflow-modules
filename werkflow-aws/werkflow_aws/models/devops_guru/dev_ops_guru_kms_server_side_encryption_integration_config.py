from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DevOpsGuruKMSServerSideEncryptionIntegrationConfig(BaseModel):
    KMSKeyId: StrictStr | None = None
    OptInStatus: Literal['ENABLED', 'DISABLED'] | None = None
    Type: Literal['CUSTOMER_MANAGED_KEY', 'AWS_OWNED_KMS_KEY'] | None = None
