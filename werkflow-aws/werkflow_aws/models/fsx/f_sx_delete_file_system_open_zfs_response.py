from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_tag import FSxTag


class FSxDeleteFileSystemOpenZFSResponse(BaseModel):
    FinalBackupId: StrictStr | None = None
    FinalBackupTags: list[FSxTag] | None = None
