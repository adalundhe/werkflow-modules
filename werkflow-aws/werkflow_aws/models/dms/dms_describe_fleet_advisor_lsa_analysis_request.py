from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeFleetAdvisorLsaAnalysisRequest(BaseModel):
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
