from __future__ import annotations
from pydantic import BaseModel
from .connect_real_time_contact_analysis_issue_detected import ConnectRealTimeContactAnalysisIssueDetected


class ConnectRealTimeContactAnalysisSegmentIssues(BaseModel):
    IssuesDetected: list[ConnectRealTimeContactAnalysisIssueDetected] | None = None
