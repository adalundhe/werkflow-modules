from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeDaemonRevisionsRequest(BaseModel):
    daemonRevisionArns: list[StrictStr]
