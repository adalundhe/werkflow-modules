from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxCreateOpenZFSOriginSnapshotConfiguration(BaseModel):
    SnapshotARN: StrictStr
    CopyStrategy: Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']
