from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMSSHPublicKey(BaseModel):
    UserName: StrictStr | None = None
    SSHPublicKeyId: StrictStr | None = None
    Fingerprint: StrictStr | None = None
    SSHPublicKeyBody: StrictStr | None = None
    Status: StrictStr | None = None
    UploadDate: datetime.datetime | StrictStr | None = None
