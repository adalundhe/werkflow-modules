from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDescribeAnalysisSchemesRequest(BaseModel):
    DomainName: StrictStr
    AnalysisSchemeNames: list[StrictStr] | None = None
    Deployed: StrictBool | None = None
