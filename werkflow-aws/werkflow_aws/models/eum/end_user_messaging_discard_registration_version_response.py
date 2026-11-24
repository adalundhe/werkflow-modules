from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_version_status_history import EndUserMessagingRegistrationVersionStatusHistory


class EndUserMessagingDiscardRegistrationVersionResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    RegistrationVersionStatus: StrictStr | None = None
    RegistrationVersionStatusHistory: EndUserMessagingRegistrationVersionStatusHistory | None = None
    ResponseMetadata: dict[str, Any] | None = None
