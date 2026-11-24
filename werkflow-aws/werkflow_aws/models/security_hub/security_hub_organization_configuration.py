from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubOrganizationConfiguration(BaseModel):
    ConfigurationType: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
