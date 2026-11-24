from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieUpdateClassificationJobRequest(BaseModel):
    jobId: StrictStr
    jobStatus: Literal['RUNNING', 'PAUSED', 'CANCELLED', 'COMPLETE', 'IDLE', 'USER_PAUSED']
