from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .end_user_messaging_registration_version_status_history import EndUserMessagingRegistrationVersionStatusHistory


class EndUserMessagingSubmitRegistrationVersionResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    RegistrationVersionStatus: StrictStr | None = None
    RegistrationVersionStatusHistory: EndUserMessagingRegistrationVersionStatusHistory | None = None
    AwsReview: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
