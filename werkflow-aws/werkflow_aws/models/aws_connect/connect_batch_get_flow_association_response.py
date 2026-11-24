from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_flow_association_summary import ConnectFlowAssociationSummary


class ConnectBatchGetFlowAssociationResponse(BaseModel):
    FlowAssociationSummaryList: list[ConnectFlowAssociationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
