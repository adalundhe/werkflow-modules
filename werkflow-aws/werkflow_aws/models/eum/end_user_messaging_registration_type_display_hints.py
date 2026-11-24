from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationTypeDisplayHints(BaseModel):
    Title: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    DocumentationTitle: StrictStr | None = None
    DocumentationLink: StrictStr | None = None
