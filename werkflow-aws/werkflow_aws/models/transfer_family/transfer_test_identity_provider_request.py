from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TransferTestIdentityProviderRequest(BaseModel):
    ServerId: StrictStr
    UserName: StrictStr
    ServerProtocol: Literal['SFTP', 'FTP', 'FTPS', 'AS2'] | None = None
    SourceIp: StrictStr | None = None
    UserPassword: StrictStr | None = None
