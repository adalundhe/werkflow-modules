from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation
from .ssm_resolved_targets import SSMResolvedTargets
from .ssm_runbook import SSMRunbook
from .ssm_target import SSMTarget


class SSMAutomationExecutionMetadata(BaseModel):
    AutomationExecutionId: StrictStr | None = None
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    AutomationExecutionStatus: StrictStr | None = None
    ExecutionStartTime: datetime.datetime | StrictStr | None = None
    ExecutionEndTime: datetime.datetime | StrictStr | None = None
    ExecutedBy: StrictStr | None = None
    LogFile: StrictStr | None = None
    Outputs: dict[StrictStr, list[StrictStr]] | None = None
    Mode: StrictStr | None = None
    ParentAutomationExecutionId: StrictStr | None = None
    CurrentStepName: StrictStr | None = None
    CurrentAction: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    WarningMessage: StrictStr | None = None
    TargetParameterName: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
    ResolvedTargets: SSMResolvedTargets | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    Target: StrictStr | None = None
    AutomationType: StrictStr | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
    TargetLocationsURL: StrictStr | None = None
    AutomationSubtype: StrictStr | None = None
    ScheduledTime: datetime.datetime | StrictStr | None = None
    Runbooks: list[SSMRunbook] | None = None
    OpsItemId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    ChangeRequestName: StrictStr | None = None
