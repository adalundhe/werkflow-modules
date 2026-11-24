from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_instance_association_output_location import SSMInstanceAssociationOutputLocation
from .ssm_target import SSMTarget
from .ssm_target_location import SSMTargetLocation


class SSMUpdateAssociationRequest(BaseModel):
    AssociationId: StrictStr
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    DocumentVersion: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    OutputLocation: SSMInstanceAssociationOutputLocation | None = None
    Name: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    AssociationName: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
    AutomationTargetParameterName: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    MaxConcurrency: StrictStr | None = None
    ComplianceSeverity: Literal['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'UNSPECIFIED'] | None = None
    SyncCompliance: Literal['AUTO', 'MANUAL'] | None = None
    ApplyOnlyAtCronInterval: StrictBool | None = None
    CalendarNames: list[StrictStr] | None = None
    TargetLocations: list[SSMTargetLocation] | None = None
    ScheduleOffset: StrictInt | None = None
    Duration: StrictInt | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    AssociationDispatchAssumeRole: StrictStr | None = None
