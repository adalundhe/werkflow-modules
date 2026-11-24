from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_replication_time_value import AWSS3ReplicationTimeValue


class AWSS3Metrics(BaseModel):
    Status: StrictStr | None = None
    EventThreshold: AWSS3ReplicationTimeValue | None = None
