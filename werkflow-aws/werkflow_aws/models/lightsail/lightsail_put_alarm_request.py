from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .lightsail_tag import LightsailTag


class LightsailPutAlarmRequest(BaseModel):
    alarmName: StrictStr
    metricName: StrictStr
    monitoredResourceName: StrictStr
    comparisonOperator: Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanThreshold', 'LessThanOrEqualToThreshold']
    threshold: StrictFloat | StrictInt
    evaluationPeriods: StrictInt
    datapointsToAlarm: StrictInt | None = None
    treatMissingData: Literal['breaching', 'notBreaching', 'ignore', 'missing'] | None = None
    contactProtocols: list[Literal['Email', 'SMS']] | None = None
    notificationTriggers: list[Literal['OK', 'ALARM', 'INSUFFICIENT_DATA']] | None = None
    notificationEnabled: StrictBool | None = None
    tags: list[LightsailTag] | None = None
