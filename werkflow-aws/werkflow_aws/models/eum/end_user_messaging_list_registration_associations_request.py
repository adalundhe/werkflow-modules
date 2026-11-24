from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_association_filter import EndUserMessagingRegistrationAssociationFilter


class EndUserMessagingListRegistrationAssociationsRequest(BaseModel):
    RegistrationId: StrictStr
    Filters: list[EndUserMessagingRegistrationAssociationFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
