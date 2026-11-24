from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_lineage_node_summary import DataZoneLineageNodeSummary


class DataZoneListLineageNodeHistoryResponse(BaseModel):
    nodes: list[DataZoneLineageNodeSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
