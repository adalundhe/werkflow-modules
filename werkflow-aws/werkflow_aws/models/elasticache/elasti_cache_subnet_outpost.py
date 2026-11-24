from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheSubnetOutpost(BaseModel):
    SubnetOutpostArn: StrictStr | None = None
