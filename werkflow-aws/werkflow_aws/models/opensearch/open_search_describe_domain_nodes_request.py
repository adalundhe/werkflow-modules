from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDomainNodesRequest(BaseModel):
    DomainName: StrictStr
