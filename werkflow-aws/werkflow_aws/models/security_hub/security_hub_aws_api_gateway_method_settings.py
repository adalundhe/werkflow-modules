from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class SecurityHubAwsApiGatewayMethodSettings(BaseModel):
    MetricsEnabled: StrictBool | None = None
    LoggingLevel: StrictStr | None = None
    DataTraceEnabled: StrictBool | None = None
    ThrottlingBurstLimit: StrictInt | None = None
    ThrottlingRateLimit: StrictFloat | StrictInt | None = None
    CachingEnabled: StrictBool | None = None
    CacheTtlInSeconds: StrictInt | None = None
    CacheDataEncrypted: StrictBool | None = None
    RequireAuthorizationForCacheControl: StrictBool | None = None
    UnauthorizedCacheControlHeaderStrategy: StrictStr | None = None
    HttpMethod: StrictStr | None = None
    ResourcePath: StrictStr | None = None
