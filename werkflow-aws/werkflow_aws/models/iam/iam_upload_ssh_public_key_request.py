from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUploadSSHPublicKeyRequest(BaseModel):
    UserName: StrictStr
    SSHPublicKeyBody: StrictStr
