from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lambda_callback_details import LambdaCallbackDetails
from .lambda_chained_invoke_details import LambdaChainedInvokeDetails
from .lambda_context_details import LambdaContextDetails
from .lambda_execution_details import LambdaExecutionDetails
from .lambda_step_details import LambdaStepDetails
from .lambda_wait_details import LambdaWaitDetails


class LambdaOperation(BaseModel):
    Id: StrictStr | None = None
    ParentId: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    SubType: StrictStr | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ExecutionDetails: LambdaExecutionDetails | None = None
    ContextDetails: LambdaContextDetails | None = None
    StepDetails: LambdaStepDetails | None = None
    WaitDetails: LambdaWaitDetails | None = None
    CallbackDetails: LambdaCallbackDetails | None = None
    ChainedInvokeDetails: LambdaChainedInvokeDetails | None = None
