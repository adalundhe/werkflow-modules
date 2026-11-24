from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .step_functions_map_run_execution_counts import StepFunctionsMapRunExecutionCounts
from .step_functions_map_run_item_counts import StepFunctionsMapRunItemCounts


class StepFunctionsDescribeMapRunResponse(BaseModel):
    mapRunArn: StrictStr | None = None
    executionArn: StrictStr | None = None
    status: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    stopDate: datetime.datetime | StrictStr | None = None
    maxConcurrency: StrictInt | None = None
    toleratedFailurePercentage: StrictFloat | StrictInt | None = None
    toleratedFailureCount: StrictInt | None = None
    itemCounts: StepFunctionsMapRunItemCounts | None = None
    executionCounts: StepFunctionsMapRunExecutionCounts | None = None
    redriveCount: StrictInt | None = None
    redriveDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
