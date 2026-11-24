from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_analysis_scheme import CloudSearchAnalysisScheme


class CloudSearchDefineAnalysisSchemeRequest(BaseModel):
    DomainName: StrictStr
    AnalysisScheme: CloudSearchAnalysisScheme
