from __future__ import annotations
from pydantic import BaseModel
from .connect_module import ConnectModule


class ConnectModules(BaseModel):
    modules: list[ConnectModule] | None = None
