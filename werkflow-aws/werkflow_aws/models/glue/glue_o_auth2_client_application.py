from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueOAuth2ClientApplication(BaseModel):
    UserManagedClientApplicationClientId: StrictStr | None = None
    AWSManagedClientApplicationReference: StrictStr | None = None
