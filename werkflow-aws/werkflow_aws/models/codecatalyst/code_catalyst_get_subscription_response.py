from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystGetSubscriptionResponse(BaseModel):
    subscriptionType: StrictStr | None = None
    awsAccountName: StrictStr | None = None
    pendingSubscriptionType: StrictStr | None = None
    pendingSubscriptionStartTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
