from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneOAuth2ClientApplication(BaseModel):
    userManagedClientApplicationClientId: StrictStr | None = None
    aWSManagedClientApplicationReference: StrictStr | None = None
