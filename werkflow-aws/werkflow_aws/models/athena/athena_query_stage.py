from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .athena_query_stage_plan_node import AthenaQueryStagePlanNode


class AthenaQueryStage(BaseModel):
    StageId: StrictInt | None = None
    State: StrictStr | None = None
    OutputBytes: StrictInt | None = None
    OutputRows: StrictInt | None = None
    InputBytes: StrictInt | None = None
    InputRows: StrictInt | None = None
    ExecutionTime: StrictInt | None = None
    QueryStagePlan: AthenaQueryStagePlanNode | None = None
    SubStages: list[AthenaQueryStage] | None = None
