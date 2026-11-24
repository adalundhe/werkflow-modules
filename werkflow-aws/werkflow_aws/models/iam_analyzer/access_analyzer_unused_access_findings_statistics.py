from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .access_analyzer_finding_aggregation_account_details import AccessAnalyzerFindingAggregationAccountDetails
from .access_analyzer_unused_access_type_statistics import AccessAnalyzerUnusedAccessTypeStatistics


class AccessAnalyzerUnusedAccessFindingsStatistics(BaseModel):
    unusedAccessTypeStatistics: list[AccessAnalyzerUnusedAccessTypeStatistics] | None = None
    topAccounts: list[AccessAnalyzerFindingAggregationAccountDetails] | None = None
    totalActiveFindings: StrictInt | None = None
    totalArchivedFindings: StrictInt | None = None
    totalResolvedFindings: StrictInt | None = None
