from __future__ import annotations
from pydantic import BaseModel
from .rds_performance_issue_details import RDSPerformanceIssueDetails


class RDSIssueDetails(BaseModel):
    PerformanceIssueDetails: RDSPerformanceIssueDetails | None = None
