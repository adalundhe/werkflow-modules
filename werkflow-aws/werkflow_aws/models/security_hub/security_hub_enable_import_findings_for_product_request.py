from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubEnableImportFindingsForProductRequest(BaseModel):
    ProductArn: StrictStr
