from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .step_functions_activity_failed_event_details import StepFunctionsActivityFailedEventDetails
from .step_functions_activity_schedule_failed_event_details import StepFunctionsActivityScheduleFailedEventDetails
from .step_functions_activity_scheduled_event_details import StepFunctionsActivityScheduledEventDetails
from .step_functions_activity_started_event_details import StepFunctionsActivityStartedEventDetails
from .step_functions_activity_succeeded_event_details import StepFunctionsActivitySucceededEventDetails
from .step_functions_activity_timed_out_event_details import StepFunctionsActivityTimedOutEventDetails
from .step_functions_evaluation_failed_event_details import StepFunctionsEvaluationFailedEventDetails
from .step_functions_execution_aborted_event_details import StepFunctionsExecutionAbortedEventDetails
from .step_functions_execution_failed_event_details import StepFunctionsExecutionFailedEventDetails
from .step_functions_execution_redriven_event_details import StepFunctionsExecutionRedrivenEventDetails
from .step_functions_execution_started_event_details import StepFunctionsExecutionStartedEventDetails
from .step_functions_execution_succeeded_event_details import StepFunctionsExecutionSucceededEventDetails
from .step_functions_execution_timed_out_event_details import StepFunctionsExecutionTimedOutEventDetails
from .step_functions_lambda_function_failed_event_details import StepFunctionsLambdaFunctionFailedEventDetails
from .step_functions_lambda_function_schedule_failed_event_details import StepFunctionsLambdaFunctionScheduleFailedEventDetails
from .step_functions_lambda_function_scheduled_event_details import StepFunctionsLambdaFunctionScheduledEventDetails
from .step_functions_lambda_function_start_failed_event_details import StepFunctionsLambdaFunctionStartFailedEventDetails
from .step_functions_lambda_function_succeeded_event_details import StepFunctionsLambdaFunctionSucceededEventDetails
from .step_functions_lambda_function_timed_out_event_details import StepFunctionsLambdaFunctionTimedOutEventDetails
from .step_functions_map_iteration_event_details import StepFunctionsMapIterationEventDetails
from .step_functions_map_run_failed_event_details import StepFunctionsMapRunFailedEventDetails
from .step_functions_map_run_redriven_event_details import StepFunctionsMapRunRedrivenEventDetails
from .step_functions_map_run_started_event_details import StepFunctionsMapRunStartedEventDetails
from .step_functions_map_state_started_event_details import StepFunctionsMapStateStartedEventDetails
from .step_functions_state_entered_event_details import StepFunctionsStateEnteredEventDetails
from .step_functions_state_exited_event_details import StepFunctionsStateExitedEventDetails
from .step_functions_task_failed_event_details import StepFunctionsTaskFailedEventDetails
from .step_functions_task_scheduled_event_details import StepFunctionsTaskScheduledEventDetails
from .step_functions_task_start_failed_event_details import StepFunctionsTaskStartFailedEventDetails
from .step_functions_task_started_event_details import StepFunctionsTaskStartedEventDetails
from .step_functions_task_submit_failed_event_details import StepFunctionsTaskSubmitFailedEventDetails
from .step_functions_task_submitted_event_details import StepFunctionsTaskSubmittedEventDetails
from .step_functions_task_succeeded_event_details import StepFunctionsTaskSucceededEventDetails
from .step_functions_task_timed_out_event_details import StepFunctionsTaskTimedOutEventDetails


class StepFunctionsHistoryEvent(BaseModel):
    timestamp: datetime.datetime | StrictStr | None = None
    type: StrictStr | None = None
    id: StrictInt | None = None
    previousEventId: StrictInt | None = None
    activityFailedEventDetails: StepFunctionsActivityFailedEventDetails | None = None
    activityScheduleFailedEventDetails: StepFunctionsActivityScheduleFailedEventDetails | None = None
    activityScheduledEventDetails: StepFunctionsActivityScheduledEventDetails | None = None
    activityStartedEventDetails: StepFunctionsActivityStartedEventDetails | None = None
    activitySucceededEventDetails: StepFunctionsActivitySucceededEventDetails | None = None
    activityTimedOutEventDetails: StepFunctionsActivityTimedOutEventDetails | None = None
    taskFailedEventDetails: StepFunctionsTaskFailedEventDetails | None = None
    taskScheduledEventDetails: StepFunctionsTaskScheduledEventDetails | None = None
    taskStartFailedEventDetails: StepFunctionsTaskStartFailedEventDetails | None = None
    taskStartedEventDetails: StepFunctionsTaskStartedEventDetails | None = None
    taskSubmitFailedEventDetails: StepFunctionsTaskSubmitFailedEventDetails | None = None
    taskSubmittedEventDetails: StepFunctionsTaskSubmittedEventDetails | None = None
    taskSucceededEventDetails: StepFunctionsTaskSucceededEventDetails | None = None
    taskTimedOutEventDetails: StepFunctionsTaskTimedOutEventDetails | None = None
    executionFailedEventDetails: StepFunctionsExecutionFailedEventDetails | None = None
    executionStartedEventDetails: StepFunctionsExecutionStartedEventDetails | None = None
    executionSucceededEventDetails: StepFunctionsExecutionSucceededEventDetails | None = None
    executionAbortedEventDetails: StepFunctionsExecutionAbortedEventDetails | None = None
    executionTimedOutEventDetails: StepFunctionsExecutionTimedOutEventDetails | None = None
    executionRedrivenEventDetails: StepFunctionsExecutionRedrivenEventDetails | None = None
    mapStateStartedEventDetails: StepFunctionsMapStateStartedEventDetails | None = None
    mapIterationStartedEventDetails: StepFunctionsMapIterationEventDetails | None = None
    mapIterationSucceededEventDetails: StepFunctionsMapIterationEventDetails | None = None
    mapIterationFailedEventDetails: StepFunctionsMapIterationEventDetails | None = None
    mapIterationAbortedEventDetails: StepFunctionsMapIterationEventDetails | None = None
    lambdaFunctionFailedEventDetails: StepFunctionsLambdaFunctionFailedEventDetails | None = None
    lambdaFunctionScheduleFailedEventDetails: StepFunctionsLambdaFunctionScheduleFailedEventDetails | None = None
    lambdaFunctionScheduledEventDetails: StepFunctionsLambdaFunctionScheduledEventDetails | None = None
    lambdaFunctionStartFailedEventDetails: StepFunctionsLambdaFunctionStartFailedEventDetails | None = None
    lambdaFunctionSucceededEventDetails: StepFunctionsLambdaFunctionSucceededEventDetails | None = None
    lambdaFunctionTimedOutEventDetails: StepFunctionsLambdaFunctionTimedOutEventDetails | None = None
    stateEnteredEventDetails: StepFunctionsStateEnteredEventDetails | None = None
    stateExitedEventDetails: StepFunctionsStateExitedEventDetails | None = None
    mapRunStartedEventDetails: StepFunctionsMapRunStartedEventDetails | None = None
    mapRunFailedEventDetails: StepFunctionsMapRunFailedEventDetails | None = None
    mapRunRedrivenEventDetails: StepFunctionsMapRunRedrivenEventDetails | None = None
    evaluationFailedEventDetails: StepFunctionsEvaluationFailedEventDetails | None = None
