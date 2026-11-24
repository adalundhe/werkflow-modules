from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt


class AWSS3TransitionInput(BaseModel):
    Date: datetime.datetime | str | None = None
    Days: StrictInt | None = None
    StorageClass: Literal['GLACIER', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'DEEP_ARCHIVE', 'GLACIER_IR'] | None = None
