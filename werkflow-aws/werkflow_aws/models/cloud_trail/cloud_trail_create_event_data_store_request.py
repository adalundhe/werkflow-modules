from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_trail_advanced_event_selector import CloudTrailAdvancedEventSelector
from .cloud_trail_tag import CloudTrailTag


class CloudTrailCreateEventDataStoreRequest(BaseModel):
    Name: StrictStr
    AdvancedEventSelectors: list[CloudTrailAdvancedEventSelector] | None = None
    MultiRegionEnabled: StrictBool | None = None
    OrganizationEnabled: StrictBool | None = None
    RetentionPeriod: StrictInt | None = None
    TerminationProtectionEnabled: StrictBool | None = None
    TagsList: list[CloudTrailTag] | None = None
    KmsKeyId: StrictStr | None = None
    StartIngestion: StrictBool | None = None
    BillingMode: Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING'] | None = None
