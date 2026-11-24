from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerFindingAggregationAccountDetails(BaseModel):
    account: StrictStr | None = None
    numberOfActiveFindings: StrictInt | None = None
    details: dict[StrictStr, StrictInt] | None = None
