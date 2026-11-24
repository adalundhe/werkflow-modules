from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool
from .f_sx_tag import FSxTag


class FSxDeleteFileSystemOpenZFSConfiguration(BaseModel):
    SkipFinalBackup: StrictBool | None = None
    FinalBackupTags: list[FSxTag] | None = None
    Options: list[Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']] | None = None
