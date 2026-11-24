from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieGetMemberResponse(BaseModel):
    accountId: StrictStr | None = None
    administratorAccountId: StrictStr | None = None
    arn: StrictStr | None = None
    email: StrictStr | None = None
    invitedAt: datetime.datetime | StrictStr | None = None
    masterAccountId: StrictStr | None = None
    relationshipStatus: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
