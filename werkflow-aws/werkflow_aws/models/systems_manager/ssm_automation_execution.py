from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation
from .ssm_progress_counters import SSMProgressCounters
from .ssm_resolved_targets import SSMResolvedTargets
from .ssm_runbook import SSMRunbook
from .ssm_step_execution import SSMStepExecution
from .ssm_target import SSMTarget
from .ssm_target_location import SSMTargetLocation
from .ssm_targets_summary import SSMTargetsSummary


class SSMAutomationExecution(BaseModel):
    AutomationExecutionId: StrictStr | None = None
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    ExecutionStartTime: datetime.datetime | StrictStr | None = None
    ExecutionEndTime: datetime.datetime | StrictStr | None = None
    AutomationExecutionStatus: StrictStr | None = None
    StepExecutions: list[SSMStepExecution] | None = None
    StepExecutionsTruncated: StrictBool | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    Outputs: dict[StrictStr, list[StrictStr]] | None = None
    FailureMessage: StrictStr | None = None
    WarningMessage: StrictStr | None = None
    Mode: StrictStr | None = None
    ParentAutomationExecutionId: StrictStr | None = None
    ExecutedBy: StrictStr | None = None
    CurrentStepName: StrictStr | None = None
    CurrentAction: StrictStr | None = None
    TargetParameterName: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
    ResolvedTargets: SSMResolvedTargets | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    Target: StrictStr | None = None
    TargetLocations: list[SSMTargetLocation] | None = None
    ProgressCounters: SSMProgressCounters | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
    TargetLocationsURL: StrictStr | None = None
    AutomationSubtype: StrictStr | None = None
    ScheduledTime: datetime.datetime | StrictStr | None = None
    Runbooks: list[SSMRunbook] | None = None
    OpsItemId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    ChangeRequestName: StrictStr | None = None
    Variables: dict[StrictStr, list[StrictStr]] | None = None
    TargetsSummary: SSMTargetsSummary | None = None
