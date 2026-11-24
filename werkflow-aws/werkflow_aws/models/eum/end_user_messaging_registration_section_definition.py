from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_section_display_hints import EndUserMessagingRegistrationSectionDisplayHints


class EndUserMessagingRegistrationSectionDefinition(BaseModel):
    SectionPath: StrictStr | None = None
    DisplayHints: EndUserMessagingRegistrationSectionDisplayHints | None = None
