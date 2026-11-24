from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .macie_finding_criteria import MacieFindingCriteria
from .macie_finding_statistics_sort_criteria import MacieFindingStatisticsSortCriteria


class MacieGetFindingStatisticsRequest(BaseModel):
    groupBy: Literal['resourcesAffected.s3Bucket.name', 'type', 'classificationDetails.jobId', 'severity.description']
    findingCriteria: MacieFindingCriteria | None = None
    size: StrictInt | None = None
    sortCriteria: MacieFindingStatisticsSortCriteria | None = None
