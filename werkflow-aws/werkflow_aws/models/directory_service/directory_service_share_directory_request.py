from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .directory_service_share_target import DirectoryServiceShareTarget


class DirectoryServiceShareDirectoryRequest(BaseModel):
    DirectoryId: StrictStr
    ShareTarget: DirectoryServiceShareTarget
    ShareMethod: Literal['ORGANIZATIONS', 'HANDSHAKE']
    ShareNotes: StrictStr | None = None
