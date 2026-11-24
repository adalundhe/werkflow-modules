from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_access_rules import LightsailAccessRules
from .lightsail_bucket_access_log_config import LightsailBucketAccessLogConfig
from .lightsail_bucket_cors_config import LightsailBucketCorsConfig


class LightsailUpdateBucketRequest(BaseModel):
    bucketName: StrictStr
    accessRules: LightsailAccessRules | None = None
    versioning: StrictStr | None = None
    readonlyAccessAccounts: list[StrictStr] | None = None
    accessLogConfig: LightsailBucketAccessLogConfig | None = None
    cors: LightsailBucketCorsConfig | None = None
