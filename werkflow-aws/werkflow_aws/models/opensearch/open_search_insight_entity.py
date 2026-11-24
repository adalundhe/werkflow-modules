from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchInsightEntity(BaseModel):
    Type: Literal['Account', 'DomainName']
    Value: StrictStr | None = None
