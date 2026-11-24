from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSListClustersResponse(BaseModel):
    clusters: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
