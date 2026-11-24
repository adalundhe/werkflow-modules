from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ECSProtectedTask(BaseModel):
    taskArn: StrictStr | None = None
    protectionEnabled: StrictBool | None = None
    expirationDate: datetime.datetime | StrictStr | None = None
