from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferListedUser(BaseModel):
    Arn: StrictStr | None = None
    HomeDirectory: StrictStr | None = None
    HomeDirectoryType: StrictStr | None = None
    Role: StrictStr | None = None
    SshPublicKeyCount: StrictInt | None = None
    UserName: StrictStr | None = None
