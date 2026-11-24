from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_query_planning_context import LakeFormationQueryPlanningContext


class LakeFormationStartQueryPlanningRequest(BaseModel):
    QueryPlanningContext: LakeFormationQueryPlanningContext
    QueryString: StrictStr
