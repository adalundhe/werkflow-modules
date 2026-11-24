from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_access_rules import LightsailAccessRules
from .lightsail_bucket_access_log_config import LightsailBucketAccessLogConfig
from .lightsail_bucket_cors_config import LightsailBucketCorsConfig
from .lightsail_bucket_state import LightsailBucketState
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_resource_receiving_access import LightsailResourceReceivingAccess
from .lightsail_tag import LightsailTag


class LightsailBucket(BaseModel):
    resourceType: StrictStr | None = None
    accessRules: LightsailAccessRules | None = None
    arn: StrictStr | None = None
    bundleId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    url: StrictStr | None = None
    location: LightsailResourceLocation | None = None
    name: StrictStr | None = None
    supportCode: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    objectVersioning: StrictStr | None = None
    ableToUpdateBundle: StrictBool | None = None
    readonlyAccessAccounts: list[StrictStr] | None = None
    resourcesReceivingAccess: list[LightsailResourceReceivingAccess] | None = None
    state: LightsailBucketState | None = None
    accessLogConfig: LightsailBucketAccessLogConfig | None = None
    cors: LightsailBucketCorsConfig | None = None
