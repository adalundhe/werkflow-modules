from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDeleteConditionalForwarderRequest(BaseModel):
    DirectoryId: StrictStr
    RemoteDomainName: StrictStr
