from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationEncryptionConfiguration(BaseModel):
    KeyType: Literal['AWS_OWNED_KEY', 'CUSTOMER_MANAGED_KEY']
    KeyId: StrictStr | None = None
