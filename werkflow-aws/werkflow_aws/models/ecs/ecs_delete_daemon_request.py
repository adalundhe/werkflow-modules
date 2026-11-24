from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeleteDaemonRequest(BaseModel):
    daemonArn: StrictStr
