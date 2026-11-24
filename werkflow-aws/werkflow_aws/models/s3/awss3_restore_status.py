from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class AWSS3RestoreStatus(BaseModel):
    IsRestoreInProgress: StrictBool | None = None
    RestoreExpiryDate: datetime.datetime | StrictStr | None = None
