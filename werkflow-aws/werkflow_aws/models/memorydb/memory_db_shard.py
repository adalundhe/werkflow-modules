from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .memory_db_node import MemoryDBNode


class MemoryDBShard(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Slots: StrictStr | None = None
    Nodes: list[MemoryDBNode] | None = None
    NumberOfNodes: StrictInt | None = None
