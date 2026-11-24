from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteSshPublicKeyRequest(BaseModel):
    ServerId: StrictStr
    SshPublicKeyId: StrictStr
    UserName: StrictStr
