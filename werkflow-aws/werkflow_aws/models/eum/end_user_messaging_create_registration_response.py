from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateRegistrationResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    RegistrationType: StrictStr | None = None
    RegistrationStatus: StrictStr | None = None
    CurrentVersionNumber: StrictInt | None = None
    AdditionalAttributes: dict[StrictStr, StrictStr] | None = None
    Tags: list[EndUserMessagingTag] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
