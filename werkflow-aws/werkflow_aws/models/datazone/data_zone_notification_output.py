from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_topic import DataZoneTopic


class DataZoneNotificationOutput(BaseModel):
    identifier: StrictStr | None = None
    domainIdentifier: StrictStr | None = None
    type: StrictStr | None = None
    topic: DataZoneTopic | None = None
    title: StrictStr | None = None
    message: StrictStr | None = None
    status: StrictStr | None = None
    actionLink: StrictStr | None = None
    creationTimestamp: datetime.datetime | StrictStr | None = None
    lastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
