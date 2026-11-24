from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_integration_association_summary import ConnectIntegrationAssociationSummary


class ConnectListIntegrationAssociationsResponse(BaseModel):
    IntegrationAssociationSummaryList: list[ConnectIntegrationAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
