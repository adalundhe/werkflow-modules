from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingGetResourcePolicyResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    Policy: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
