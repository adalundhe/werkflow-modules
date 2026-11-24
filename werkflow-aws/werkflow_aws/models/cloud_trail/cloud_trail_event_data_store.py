from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_trail_advanced_event_selector import CloudTrailAdvancedEventSelector


class CloudTrailEventDataStore(BaseModel):
    EventDataStoreArn: StrictStr | None = None
    Name: StrictStr | None = None
    TerminationProtectionEnabled: StrictBool | None = None
    Status: StrictStr | None = None
    AdvancedEventSelectors: list[CloudTrailAdvancedEventSelector] | None = None
    MultiRegionEnabled: StrictBool | None = None
    OrganizationEnabled: StrictBool | None = None
    RetentionPeriod: StrictInt | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    UpdatedTimestamp: datetime.datetime | StrictStr | None = None
