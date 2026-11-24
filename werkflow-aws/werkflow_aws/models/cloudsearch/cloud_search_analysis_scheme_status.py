from __future__ import annotations
from pydantic import BaseModel
from .cloud_search_analysis_scheme import CloudSearchAnalysisScheme
from .cloud_search_option_status import CloudSearchOptionStatus


class CloudSearchAnalysisSchemeStatus(BaseModel):
    Options: CloudSearchAnalysisScheme | None = None
    Status: CloudSearchOptionStatus | None = None
