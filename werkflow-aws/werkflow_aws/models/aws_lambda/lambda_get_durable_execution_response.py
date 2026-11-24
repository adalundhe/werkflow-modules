from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .lambda_durable_config_model import LambdaDurableConfigModel
from .lambda_error_object import LambdaErrorObject
from .lambda_pause_details import LambdaPauseDetails
from .lambda_trace_header import LambdaTraceHeader


class LambdaGetDurableExecutionResponse(BaseModel):
    DurableExecutionArn: StrictStr | None = None
    DurableExecutionName: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    InputPayload: StrictStr | None = None
    Result: StrictStr | None = None
    Error: LambdaErrorObject | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    Version: StrictStr | None = None
    TraceHeader: LambdaTraceHeader | None = None
    ExecutionDataIncluded: StrictBool | None = None
    DurableConfig: LambdaDurableConfigModel | None = None
    PauseDetails: LambdaPauseDetails | None = None
    ExpectedExecutionTimeoutTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
