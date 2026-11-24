from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_alarm_state_information import SSMAlarmStateInformation
from .ssm_failure_details import SSMFailureDetails
from .ssm_parent_step_details import SSMParentStepDetails
from .ssm_target import SSMTarget
from .ssm_target_location import SSMTargetLocation


class SSMStepExecution(BaseModel):
    StepName: StrictStr | None = None
    Action: StrictStr | None = None
    TimeoutSeconds: StrictInt | None = None
    OnFailure: StrictStr | None = None
    MaxAttempts: StrictInt | None = None
    ExecutionStartTime: datetime.datetime | StrictStr | None = None
    ExecutionEndTime: datetime.datetime | StrictStr | None = None
    StepStatus: StrictStr | None = None
    ResponseCode: StrictStr | None = None
    Inputs: dict[StrictStr, StrictStr] | None = None
    Outputs: dict[StrictStr, list[StrictStr]] | None = None
    Response: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    WarningMessage: StrictStr | None = None
    FailureDetails: SSMFailureDetails | None = None
    StepExecutionId: StrictStr | None = None
    OverriddenParameters: dict[StrictStr, list[StrictStr]] | None = None
    IsEnd: StrictBool | None = None
    NextStep: StrictStr | None = None
    IsCritical: StrictBool | None = None
    ValidNextSteps: list[StrictStr] | None = None
    Targets: list[SSMTarget] | None = None
    TargetLocation: SSMTargetLocation | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
    ParentStepDetails: SSMParentStepDetails | None = None
