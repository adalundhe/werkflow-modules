from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_analysis_scheme_status import CloudSearchAnalysisSchemeStatus


class CloudSearchDescribeAnalysisSchemesResponse(BaseModel):
    AnalysisSchemes: list[CloudSearchAnalysisSchemeStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
