from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation
from .ssm_association_overview import SSMAssociationOverview
from .ssm_association_status import SSMAssociationStatus
from .ssm_instance_association_output_location import SSMInstanceAssociationOutputLocation
from .ssm_target import SSMTarget
from .ssm_target_location import SSMTargetLocation


class SSMAssociationDescription(BaseModel):
    Name: StrictStr | None = None
    InstanceId: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
    Date: datetime.datetime | StrictStr | None = None
    LastUpdateAssociationDate: datetime.datetime | StrictStr | None = None
    Status: SSMAssociationStatus | None = None
    Overview: SSMAssociationOverview | None = None
    DocumentVersion: StrictStr | None = None
    AutomationTargetParameterName: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    AssociationId: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    ScheduleExpression: StrictStr | None = None
    OutputLocation: SSMInstanceAssociationOutputLocation | None = None
    LastExecutionDate: datetime.datetime | StrictStr | None = None
    LastSuccessfulExecutionDate: datetime.datetime | StrictStr | None = None
    AssociationName: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    MaxConcurrency: StrictStr | None = None
    ComplianceSeverity: StrictStr | None = None
    SyncCompliance: StrictStr | None = None
    ApplyOnlyAtCronInterval: StrictBool | None = None
    CalendarNames: list[StrictStr] | None = None
    TargetLocations: list[SSMTargetLocation] | None = None
    ScheduleOffset: StrictInt | None = None
    Duration: StrictInt | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
    AssociationDispatchAssumeRole: StrictStr | None = None
