from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubJiraCloudProviderConfiguration(BaseModel):
    ProjectKey: StrictStr | None = None
