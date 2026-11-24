from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationEncryptionConfigurationUpdate(BaseModel):
    KeyTypeUpdate: Literal['AWS_OWNED_KEY', 'CUSTOMER_MANAGED_KEY']
    KeyIdUpdate: StrictStr | None = None
