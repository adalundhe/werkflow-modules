from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubServiceNowUpdateConfiguration(BaseModel):
    SecretArn: StrictStr | None = None
