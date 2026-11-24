from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESSendCustomVerificationEmailRequest(BaseModel):
    EmailAddress: StrictStr
    TemplateName: StrictStr
    ConfigurationSetName: StrictStr | None = None
