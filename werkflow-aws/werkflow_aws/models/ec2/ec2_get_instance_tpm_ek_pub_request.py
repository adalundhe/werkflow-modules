from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetInstanceTpmEkPubRequest(BaseModel):
    InstanceId: StrictStr
    KeyType: Literal['rsa-2048', 'ecc-sec-p384']
    KeyFormat: Literal['der', 'tpmt']
    DryRun: StrictBool | None = None
