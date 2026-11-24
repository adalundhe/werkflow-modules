from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_tag import FSxTag


class FSxCreateBackupRequest(BaseModel):
    FileSystemId: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    VolumeId: StrictStr | None = None
