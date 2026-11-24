from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_tag import SSMTag
from .ssm_target import SSMTarget
from .ssm_target_location import SSMTargetLocation


class SSMStartAutomationExecutionRequest(BaseModel):
    DocumentName: StrictStr
    DocumentVersion: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    ClientToken: StrictStr | None = None
    Mode: Literal['Auto', 'Interactive'] | None = None
    TargetParameterName: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    TargetLocations: list[SSMTargetLocation] | None = None
    Tags: list[SSMTag] | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TargetLocationsURL: StrictStr | None = None
