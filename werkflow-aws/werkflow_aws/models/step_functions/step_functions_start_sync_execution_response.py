from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_billing_details import StepFunctionsBillingDetails
from .step_functions_cloud_watch_events_execution_data_details import StepFunctionsCloudWatchEventsExecutionDataDetails


class StepFunctionsStartSyncExecutionResponse(BaseModel):
    executionArn: StrictStr | None = None
    stateMachineArn: StrictStr | None = None
    name: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    stopDate: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    error: StrictStr | None = None
    cause: StrictStr | None = None
    input: StrictStr | None = None
    inputDetails: StepFunctionsCloudWatchEventsExecutionDataDetails | None = None
    output: StrictStr | None = None
    outputDetails: StepFunctionsCloudWatchEventsExecutionDataDetails | None = None
    traceHeader: StrictStr | None = None
    billingDetails: StepFunctionsBillingDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
