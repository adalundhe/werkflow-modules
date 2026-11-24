from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubJiraCloudDetail(BaseModel):
    CloudId: StrictStr | None = None
    ProjectKey: StrictStr | None = None
    Domain: StrictStr | None = None
    AuthUrl: StrictStr | None = None
    AuthStatus: StrictStr | None = None
