from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectRecommenderConfig(BaseModel):
    DomainName: StrictStr
    RecommenderName: StrictStr
    Context: dict[StrictStr, StrictStr] | None = None
