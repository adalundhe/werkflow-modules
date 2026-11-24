from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3ReplicationTimeValue(BaseModel):
    Minutes: StrictInt | None = None
