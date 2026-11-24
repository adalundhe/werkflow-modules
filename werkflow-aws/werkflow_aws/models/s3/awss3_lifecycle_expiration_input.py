from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt


class AWSS3LifecycleExpirationInput(BaseModel):
    Date: datetime.datetime | str | None = None
    Days: StrictInt | None = None
    ExpiredObjectDeleteMarker: StrictBool | None = None
