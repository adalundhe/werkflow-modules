from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_analysis_options import CloudSearchAnalysisOptions


class CloudSearchAnalysisScheme(BaseModel):
    AnalysisSchemeName: StrictStr | None = None
    AnalysisSchemeLanguage: StrictStr | None = None
    AnalysisOptions: CloudSearchAnalysisOptions | None = None
