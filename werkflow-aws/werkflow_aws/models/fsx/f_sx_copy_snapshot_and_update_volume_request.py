from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxCopySnapshotAndUpdateVolumeRequest(BaseModel):
    VolumeId: StrictStr
    SourceSnapshotARN: StrictStr
    ClientRequestToken: StrictStr | None = None
    CopyStrategy: Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY'] | None = None
    Options: list[Literal['DELETE_INTERMEDIATE_SNAPSHOTS', 'DELETE_CLONED_VOLUMES', 'DELETE_INTERMEDIATE_DATA']] | None = None
