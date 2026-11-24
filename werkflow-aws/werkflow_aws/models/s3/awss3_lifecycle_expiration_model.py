from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AWSS3LifecycleExpirationModel(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    Days: StrictInt | None = None
    ExpiredObjectDeleteMarker: StrictBool | None = None
