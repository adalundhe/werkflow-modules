from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AppFlowSAPODataParallelismConfig(BaseModel):
    maxParallelism: StrictInt | None = None
