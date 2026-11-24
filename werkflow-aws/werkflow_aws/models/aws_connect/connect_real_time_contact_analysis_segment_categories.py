from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_category_details import ConnectRealTimeContactAnalysisCategoryDetails


class ConnectRealTimeContactAnalysisSegmentCategories(BaseModel):
    MatchedDetails: dict[StrictStr, ConnectRealTimeContactAnalysisCategoryDetails] | None = None
