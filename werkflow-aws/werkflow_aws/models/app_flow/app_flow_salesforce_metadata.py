from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSalesforceMetadata(BaseModel):
    oAuthScopes: list[StrictStr] | None = None
    dataTransferApis: list[StrictStr] | None = None
    oauth2GrantTypesSupported: list[StrictStr] | None = None
