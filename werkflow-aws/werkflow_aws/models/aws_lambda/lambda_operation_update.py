from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lambda_callback_options import LambdaCallbackOptions
from .lambda_chained_invoke_options import LambdaChainedInvokeOptions
from .lambda_context_options import LambdaContextOptions
from .lambda_error_object import LambdaErrorObject
from .lambda_step_options import LambdaStepOptions
from .lambda_wait_options import LambdaWaitOptions


class LambdaOperationUpdate(BaseModel):
    Id: StrictStr
    Type: Literal['EXECUTION', 'CONTEXT', 'STEP', 'WAIT', 'CALLBACK', 'CHAINED_INVOKE']
    Action: Literal['START', 'SUCCEED', 'FAIL', 'RETRY', 'CANCEL']
    ParentId: StrictStr | None = None
    Name: StrictStr | None = None
    SubType: StrictStr | None = None
    Payload: StrictStr | None = None
    Error: LambdaErrorObject | None = None
    ContextOptions: LambdaContextOptions | None = None
    StepOptions: LambdaStepOptions | None = None
    WaitOptions: LambdaWaitOptions | None = None
    CallbackOptions: LambdaCallbackOptions | None = None
    ChainedInvokeOptions: LambdaChainedInvokeOptions | None = None
