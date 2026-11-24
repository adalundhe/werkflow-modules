from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_action_connector_search_filter import QuickSightActionConnectorSearchFilter


class QuickSightSearchActionConnectorsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightActionConnectorSearchFilter]
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
