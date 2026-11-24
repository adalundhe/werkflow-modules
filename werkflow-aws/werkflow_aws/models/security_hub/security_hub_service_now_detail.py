from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubServiceNowDetail(BaseModel):
    InstanceName: StrictStr | None = None
    SecretArn: StrictStr | None = None
    AuthStatus: StrictStr | None = None
