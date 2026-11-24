from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ComputeOptimizerGetEnrollmentStatusResponse(BaseModel):
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    memberAccountsEnrolled: StrictBool | None = None
    lastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    numberOfMemberAccountsOptedIn: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
