from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMSSHPublicKeyMetadata(BaseModel):
    UserName: StrictStr | None = None
    SSHPublicKeyId: StrictStr | None = None
    Status: StrictStr | None = None
    UploadDate: datetime.datetime | StrictStr | None = None
