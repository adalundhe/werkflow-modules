from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag
from .ses_topic import SESTopic


class SESGetContactListResponse(BaseModel):
    ContactListName: StrictStr | None = None
    Topics: list[SESTopic] | None = None
    Description: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    Tags: list[SESTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
