from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSListSubscriptionsRequest(BaseModel):
    NextToken: StrictStr | None = None
