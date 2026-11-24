from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListClustersRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    include: list[StrictStr] | None = None
