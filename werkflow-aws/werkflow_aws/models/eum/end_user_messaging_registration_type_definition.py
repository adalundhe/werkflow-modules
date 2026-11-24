from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_type_display_hints import EndUserMessagingRegistrationTypeDisplayHints
from .end_user_messaging_supported_association import EndUserMessagingSupportedAssociation


class EndUserMessagingRegistrationTypeDefinition(BaseModel):
    RegistrationType: StrictStr | None = None
    SupportedAssociations: list[EndUserMessagingSupportedAssociation] | None = None
    DisplayHints: EndUserMessagingRegistrationTypeDisplayHints | None = None
