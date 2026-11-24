from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_flow_association_summary import ConnectFlowAssociationSummary


class ConnectListFlowAssociationsResponse(BaseModel):
    FlowAssociationSummaryList: list[ConnectFlowAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
