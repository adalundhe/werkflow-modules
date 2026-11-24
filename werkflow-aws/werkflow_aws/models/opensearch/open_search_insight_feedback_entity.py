from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchInsightFeedbackEntity(BaseModel):
    Type: Literal['DomainName']
    Value: StrictStr
