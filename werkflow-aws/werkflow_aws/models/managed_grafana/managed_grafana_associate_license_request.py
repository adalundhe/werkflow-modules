from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ManagedGrafanaAssociateLicenseRequest(BaseModel):
    workspaceId: StrictStr
    licenseType: Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']
    grafanaToken: StrictStr | None = None
