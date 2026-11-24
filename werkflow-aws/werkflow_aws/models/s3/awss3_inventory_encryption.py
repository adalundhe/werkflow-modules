from __future__ import annotations
from pydantic import BaseModel
from .awss3_ssekms import AWSS3SSEKMS
from .awss3_sses3 import AWSS3SSES3


class AWSS3InventoryEncryption(BaseModel):
    SSES3: AWSS3SSES3 | None = None
    SSEKMS: AWSS3SSEKMS | None = None
