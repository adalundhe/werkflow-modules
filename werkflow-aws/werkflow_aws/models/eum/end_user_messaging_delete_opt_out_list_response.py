from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteOptOutListResponse(BaseModel):
    OptOutListArn: StrictStr | None = None
    OptOutListName: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
