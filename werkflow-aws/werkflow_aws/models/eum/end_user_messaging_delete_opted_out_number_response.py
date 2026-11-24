from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingDeleteOptedOutNumberResponse(BaseModel):
    OptOutListArn: StrictStr | None = None
    OptOutListName: StrictStr | None = None
    OptedOutNumber: StrictStr | None = None
    OptedOutTimestamp: datetime.datetime | StrictStr | None = None
    EndUserOptedOut: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
