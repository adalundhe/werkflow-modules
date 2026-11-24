from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_execution_statistics import LakeFormationExecutionStatistics
from .lake_formation_planning_statistics import LakeFormationPlanningStatistics


class LakeFormationGetQueryStatisticsResponse(BaseModel):
    ExecutionStatistics: LakeFormationExecutionStatistics | None = None
    PlanningStatistics: LakeFormationPlanningStatistics | None = None
    QuerySubmissionTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
