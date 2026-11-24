from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationDeniedReasonInformation(BaseModel):
    Reason: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    DocumentationTitle: StrictStr | None = None
    DocumentationLink: StrictStr | None = None
