from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteSSHPublicKeyRequest(BaseModel):
    UserName: StrictStr
    SSHPublicKeyId: StrictStr
