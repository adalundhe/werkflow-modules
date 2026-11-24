from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingCreateRegistrationAssociationResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    RegistrationType: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
