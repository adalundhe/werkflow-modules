from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRemediationStep(BaseModel):
    Phase: StrictStr | None = None
    Description: StrictStr | None = None
    Service: StrictStr | None = None
    Action: StrictStr | None = None
    Logic: StrictStr | None = None
    Inverse: StrictStr | None = None
    VerifyAfter: StrictStr | None = None
