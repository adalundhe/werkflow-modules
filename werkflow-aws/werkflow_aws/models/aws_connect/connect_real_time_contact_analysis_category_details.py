from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_point_of_interest import ConnectRealTimeContactAnalysisPointOfInterest


class ConnectRealTimeContactAnalysisCategoryDetails(BaseModel):
    RuleId: StrictStr | None = None
    PointsOfInterest: list[ConnectRealTimeContactAnalysisPointOfInterest] | None = None
