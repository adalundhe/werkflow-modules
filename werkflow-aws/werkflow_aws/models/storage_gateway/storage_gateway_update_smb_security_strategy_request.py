from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateSMBSecurityStrategyRequest(BaseModel):
    GatewayARN: StrictStr
    SMBSecurityStrategy: Literal['ClientSpecified', 'MandatorySigning', 'MandatoryEncryption', 'MandatoryEncryptionNoAes128']
