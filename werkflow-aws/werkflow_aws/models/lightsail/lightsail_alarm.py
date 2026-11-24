from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .lightsail_monitored_resource_info import LightsailMonitoredResourceInfo
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailAlarm(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    supportCode: StrictStr | None = None
    monitoredResourceInfo: LightsailMonitoredResourceInfo | None = None
    comparisonOperator: StrictStr | None = None
    evaluationPeriods: StrictInt | None = None
    period: StrictInt | None = None
    threshold: StrictFloat | StrictInt | None = None
    datapointsToAlarm: StrictInt | None = None
    treatMissingData: StrictStr | None = None
    statistic: StrictStr | None = None
    metricName: StrictStr | None = None
    state: StrictStr | None = None
    unit: StrictStr | None = None
    contactProtocols: list[StrictStr] | None = None
    notificationTriggers: list[StrictStr] | None = None
    notificationEnabled: StrictBool | None = None
    tags: list[LightsailTag] | None = None
