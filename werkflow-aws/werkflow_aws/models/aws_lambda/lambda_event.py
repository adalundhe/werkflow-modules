from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_callback_failed_details import LambdaCallbackFailedDetails
from .lambda_callback_started_details import LambdaCallbackStartedDetails
from .lambda_callback_succeeded_details import LambdaCallbackSucceededDetails
from .lambda_callback_timed_out_details import LambdaCallbackTimedOutDetails
from .lambda_chained_invoke_failed_details import LambdaChainedInvokeFailedDetails
from .lambda_chained_invoke_started_details import LambdaChainedInvokeStartedDetails
from .lambda_chained_invoke_stopped_details import LambdaChainedInvokeStoppedDetails
from .lambda_chained_invoke_succeeded_details import LambdaChainedInvokeSucceededDetails
from .lambda_chained_invoke_timed_out_details import LambdaChainedInvokeTimedOutDetails
from .lambda_context_failed_details import LambdaContextFailedDetails
from .lambda_context_started_details import LambdaContextStartedDetails
from .lambda_context_succeeded_details import LambdaContextSucceededDetails
from .lambda_execution_failed_details import LambdaExecutionFailedDetails
from .lambda_execution_paused_details import LambdaExecutionPausedDetails
from .lambda_execution_resumed_details import LambdaExecutionResumedDetails
from .lambda_execution_started_details import LambdaExecutionStartedDetails
from .lambda_execution_stopped_details import LambdaExecutionStoppedDetails
from .lambda_execution_succeeded_details import LambdaExecutionSucceededDetails
from .lambda_execution_timed_out_details import LambdaExecutionTimedOutDetails
from .lambda_invocation_completed_details import LambdaInvocationCompletedDetails
from .lambda_step_failed_details import LambdaStepFailedDetails
from .lambda_step_started_details import LambdaStepStartedDetails
from .lambda_step_succeeded_details import LambdaStepSucceededDetails
from .lambda_wait_cancelled_details import LambdaWaitCancelledDetails
from .lambda_wait_started_details import LambdaWaitStartedDetails
from .lambda_wait_succeeded_details import LambdaWaitSucceededDetails


class LambdaEvent(BaseModel):
    EventType: StrictStr | None = None
    SubType: StrictStr | None = None
    EventId: StrictInt | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    EventTimestamp: datetime.datetime | StrictStr | None = None
    ParentId: StrictStr | None = None
    ExecutionStartedDetails: LambdaExecutionStartedDetails | None = None
    ExecutionSucceededDetails: LambdaExecutionSucceededDetails | None = None
    ExecutionFailedDetails: LambdaExecutionFailedDetails | None = None
    ExecutionTimedOutDetails: LambdaExecutionTimedOutDetails | None = None
    ExecutionStoppedDetails: LambdaExecutionStoppedDetails | None = None
    ContextStartedDetails: LambdaContextStartedDetails | None = None
    ContextSucceededDetails: LambdaContextSucceededDetails | None = None
    ContextFailedDetails: LambdaContextFailedDetails | None = None
    WaitStartedDetails: LambdaWaitStartedDetails | None = None
    WaitSucceededDetails: LambdaWaitSucceededDetails | None = None
    WaitCancelledDetails: LambdaWaitCancelledDetails | None = None
    StepStartedDetails: LambdaStepStartedDetails | None = None
    StepSucceededDetails: LambdaStepSucceededDetails | None = None
    StepFailedDetails: LambdaStepFailedDetails | None = None
    ChainedInvokeStartedDetails: LambdaChainedInvokeStartedDetails | None = None
    ChainedInvokeSucceededDetails: LambdaChainedInvokeSucceededDetails | None = None
    ChainedInvokeFailedDetails: LambdaChainedInvokeFailedDetails | None = None
    ChainedInvokeTimedOutDetails: LambdaChainedInvokeTimedOutDetails | None = None
    ChainedInvokeStoppedDetails: LambdaChainedInvokeStoppedDetails | None = None
    CallbackStartedDetails: LambdaCallbackStartedDetails | None = None
    CallbackSucceededDetails: LambdaCallbackSucceededDetails | None = None
    CallbackFailedDetails: LambdaCallbackFailedDetails | None = None
    CallbackTimedOutDetails: LambdaCallbackTimedOutDetails | None = None
    InvocationCompletedDetails: LambdaInvocationCompletedDetails | None = None
    ExecutionPausedDetails: LambdaExecutionPausedDetails | None = None
    ExecutionResumedDetails: LambdaExecutionResumedDetails | None = None
