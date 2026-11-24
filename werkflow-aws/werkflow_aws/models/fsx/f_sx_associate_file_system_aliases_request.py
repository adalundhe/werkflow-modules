from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxAssociateFileSystemAliasesRequest(BaseModel):
    FileSystemId: StrictStr
    Aliases: list[StrictStr]
    ClientRequestToken: StrictStr | None = None
