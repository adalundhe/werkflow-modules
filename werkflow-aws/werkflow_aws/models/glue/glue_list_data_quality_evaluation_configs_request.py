from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListDataQualityEvaluationConfigsRequest(BaseModel):
    Level: Literal['CATALOG', 'DATABASE', 'TABLE'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
