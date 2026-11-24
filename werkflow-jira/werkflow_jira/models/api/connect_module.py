from __future__ import annotations
from pydantic import BaseModel, ConfigDict


class ConnectModule(BaseModel):
    model_config = ConfigDict(extra="allow")
