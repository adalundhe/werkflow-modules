from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateVerifiedDestinationNumberResponse(BaseModel):
    VerifiedDestinationNumberArn: StrictStr | None = None
    VerifiedDestinationNumberId: StrictStr | None = None
    DestinationPhoneNumber: StrictStr | None = None
    Status: StrictStr | None = None
    RcsAgentId: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
