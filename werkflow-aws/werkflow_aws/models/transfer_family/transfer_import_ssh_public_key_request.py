from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferImportSshPublicKeyRequest(BaseModel):
    ServerId: StrictStr
    SshPublicKeyBody: StrictStr
    UserName: StrictStr
