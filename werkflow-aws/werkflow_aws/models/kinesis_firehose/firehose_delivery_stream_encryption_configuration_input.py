from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FirehoseDeliveryStreamEncryptionConfigurationInput(BaseModel):
    KeyType: Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']
    KeyARN: StrictStr | None = None
