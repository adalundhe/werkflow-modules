from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt


class AWSS3LifecycleExpiration(BaseModel):
    Date: datetime.datetime | None = None
    Days: StrictInt | None = None
    ExpiredObjectDeleteMarker: StrictBool | None = None
