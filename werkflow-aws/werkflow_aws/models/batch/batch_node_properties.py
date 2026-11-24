from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_node_range_property import BatchNodeRangeProperty


class BatchNodeProperties(BaseModel):
    numNodes: StrictInt | None = None
    mainNode: StrictInt | None = None
    nodeRangeProperties: list[BatchNodeRangeProperty] | None = None
