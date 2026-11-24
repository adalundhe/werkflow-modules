from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKReplicationTopicNameConfiguration(BaseModel):
    Type: StrictStr | None = None
