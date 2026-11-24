from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .f_sx_tag import FSxTag


class FSxCopyBackupRequest(BaseModel):
    SourceBackupId: StrictStr
    ClientRequestToken: StrictStr | None = None
    SourceRegion: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    CopyTags: StrictBool | None = None
    Tags: list[FSxTag] | None = None
