from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IAMGetSSHPublicKeyRequest(BaseModel):
    UserName: StrictStr
    SSHPublicKeyId: StrictStr
    Encoding: Literal['SSH', 'PEM']
