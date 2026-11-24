from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBReplica(BaseModel):
    RegionName: StrictStr | None = None
