from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .step_functions_cloud_watch_events_execution_data_details import StepFunctionsCloudWatchEventsExecutionDataDetails


class StepFunctionsDescribeExecutionResponse(BaseModel):
    executionArn: StrictStr | None = None
    stateMachineArn: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    stopDate: datetime.datetime | StrictStr | None = None
    input: StrictStr | None = None
    inputDetails: StepFunctionsCloudWatchEventsExecutionDataDetails | None = None
    output: StrictStr | None = None
    outputDetails: StepFunctionsCloudWatchEventsExecutionDataDetails | None = None
    traceHeader: StrictStr | None = None
    mapRunArn: StrictStr | None = None
    error: StrictStr | None = None
    cause: StrictStr | None = None
    stateMachineVersionArn: StrictStr | None = None
    stateMachineAliasArn: StrictStr | None = None
    redriveCount: StrictInt | None = None
    redriveDate: datetime.datetime | StrictStr | None = None
    redriveStatus: StrictStr | None = None
    redriveStatusReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
