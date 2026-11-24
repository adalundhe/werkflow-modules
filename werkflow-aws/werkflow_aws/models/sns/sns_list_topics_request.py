from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSListTopicsRequest(BaseModel):
    NextToken: StrictStr | None = None
