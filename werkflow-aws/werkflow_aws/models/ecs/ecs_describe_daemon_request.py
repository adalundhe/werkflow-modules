from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeDaemonRequest(BaseModel):
    daemonArn: StrictStr
