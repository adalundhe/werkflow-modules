from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDeleteAnalysisSchemeRequest(BaseModel):
    DomainName: StrictStr
    AnalysisSchemeName: StrictStr
