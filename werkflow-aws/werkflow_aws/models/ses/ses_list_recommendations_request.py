from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListRecommendationsRequest(BaseModel):
    Filter: dict[Literal['TYPE', 'IMPACT', 'STATUS', 'RESOURCE_ARN'], StrictStr] | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
