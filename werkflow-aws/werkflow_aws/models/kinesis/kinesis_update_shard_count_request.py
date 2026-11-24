from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisUpdateShardCountRequest(BaseModel):
    TargetShardCount: StrictInt
    ScalingType: Literal['UNIFORM_SCALING']
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
