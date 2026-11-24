from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_node_property_override import BatchNodePropertyOverride


class BatchNodeOverrides(BaseModel):
    numNodes: StrictInt | None = None
    nodePropertyOverrides: list[BatchNodePropertyOverride] | None = None
