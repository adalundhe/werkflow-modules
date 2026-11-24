from __future__ import annotations
from pydantic import BaseModel
from .data_zone_lineage_node_item import DataZoneLineageNodeItem


class DataZoneResultItem(BaseModel):
    lineageNode: DataZoneLineageNodeItem | None = None
