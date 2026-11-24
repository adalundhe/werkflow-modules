from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .f_sx_tag import FSxTag


class FSxDeleteFileSystemWindowsConfiguration(BaseModel):
    SkipFinalBackup: StrictBool | None = None
    FinalBackupTags: list[FSxTag] | None = None
