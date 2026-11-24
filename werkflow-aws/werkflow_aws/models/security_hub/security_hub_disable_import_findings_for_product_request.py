from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDisableImportFindingsForProductRequest(BaseModel):
    ProductSubscriptionArn: StrictStr
