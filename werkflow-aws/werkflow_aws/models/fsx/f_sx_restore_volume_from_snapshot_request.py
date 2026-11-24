from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxRestoreVolumeFromSnapshotRequest(BaseModel):
    VolumeId: StrictStr
    SnapshotId: StrictStr
    ClientRequestToken: StrictStr | None = None
    Options: list[Literal['DELETE_INTERMEDIATE_SNAPSHOTS', 'DELETE_CLONED_VOLUMES']] | None = None
