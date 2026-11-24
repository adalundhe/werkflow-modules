from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_replication_time_value import AWSS3ReplicationTimeValue


class AWSS3ReplicationTime(BaseModel):
    Status: StrictStr | None = None
    Time: AWSS3ReplicationTimeValue | None = None
