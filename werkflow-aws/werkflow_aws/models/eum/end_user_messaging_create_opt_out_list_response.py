from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateOptOutListResponse(BaseModel):
    OptOutListArn: StrictStr | None = None
    OptOutListName: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
