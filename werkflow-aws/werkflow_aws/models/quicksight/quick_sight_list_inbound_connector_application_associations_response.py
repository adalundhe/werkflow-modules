from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_inbound_connector_application_association_summary import QuickSightInboundConnectorApplicationAssociationSummary


class QuickSightListInboundConnectorApplicationAssociationsResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ApplicationAssociations: list[QuickSightInboundConnectorApplicationAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
