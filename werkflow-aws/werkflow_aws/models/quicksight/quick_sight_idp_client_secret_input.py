from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightIdpClientSecretInput(BaseModel):
    RegionalSecretManagerArns: dict[StrictStr, StrictStr]
