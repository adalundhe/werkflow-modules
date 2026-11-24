from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPRestorationDescriptionType(BaseModel):
    RestoreId: StrictStr | None = None
    RestoreStatus: StrictStr | None = None
    RestoreTimestamp: datetime.datetime | StrictStr | None = None
