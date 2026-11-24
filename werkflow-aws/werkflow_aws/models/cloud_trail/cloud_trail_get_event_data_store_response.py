from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_trail_advanced_event_selector import CloudTrailAdvancedEventSelector
from .cloud_trail_partition_key import CloudTrailPartitionKey


class CloudTrailGetEventDataStoreResponse(BaseModel):
    EventDataStoreArn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    AdvancedEventSelectors: list[CloudTrailAdvancedEventSelector] | None = None
    MultiRegionEnabled: StrictBool | None = None
    OrganizationEnabled: StrictBool | None = None
    RetentionPeriod: StrictInt | None = None
    TerminationProtectionEnabled: StrictBool | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    UpdatedTimestamp: datetime.datetime | StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    BillingMode: StrictStr | None = None
    FederationStatus: StrictStr | None = None
    FederationRoleArn: StrictStr | None = None
    PartitionKeys: list[CloudTrailPartitionKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
