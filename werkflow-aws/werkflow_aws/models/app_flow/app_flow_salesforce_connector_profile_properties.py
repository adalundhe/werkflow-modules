from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowSalesforceConnectorProfileProperties(BaseModel):
    instanceUrl: StrictStr | None = None
    isSandboxEnvironment: StrictBool | None = None
    usePrivateLinkForMetadataAndAuthorization: StrictBool | None = None
