from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubJiraCloudUpdateConfiguration(BaseModel):
    ProjectKey: StrictStr | None = None
