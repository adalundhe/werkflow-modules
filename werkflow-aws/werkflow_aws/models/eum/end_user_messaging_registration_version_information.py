from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_denied_reason_information import EndUserMessagingRegistrationDeniedReasonInformation
from .end_user_messaging_registration_version_status_history import EndUserMessagingRegistrationVersionStatusHistory


class EndUserMessagingRegistrationVersionInformation(BaseModel):
    VersionNumber: StrictInt | None = None
    RegistrationVersionStatus: StrictStr | None = None
    RegistrationVersionStatusHistory: EndUserMessagingRegistrationVersionStatusHistory | None = None
    DeniedReasons: list[EndUserMessagingRegistrationDeniedReasonInformation] | None = None
    Feedback: StrictStr | None = None
