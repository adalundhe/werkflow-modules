from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_association_metadata import EndUserMessagingRegistrationAssociationMetadata


class EndUserMessagingListRegistrationAssociationsResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    RegistrationType: StrictStr | None = None
    RegistrationAssociations: list[EndUserMessagingRegistrationAssociationMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
