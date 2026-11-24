from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESMailFromAttributes(BaseModel):
    MailFromDomain: StrictStr | None = None
    MailFromDomainStatus: StrictStr | None = None
    BehaviorOnMxFailure: StrictStr | None = None
