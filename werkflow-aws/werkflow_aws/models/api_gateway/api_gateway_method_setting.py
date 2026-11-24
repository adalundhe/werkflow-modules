from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class APIGatewayMethodSetting(BaseModel):
    metricsEnabled: StrictBool | None = None
    loggingLevel: StrictStr | None = None
    dataTraceEnabled: StrictBool | None = None
    throttlingBurstLimit: StrictInt | None = None
    throttlingRateLimit: StrictFloat | StrictInt | None = None
    cachingEnabled: StrictBool | None = None
    cacheTtlInSeconds: StrictInt | None = None
    cacheDataEncrypted: StrictBool | None = None
    requireAuthorizationForCacheControl: StrictBool | None = None
    unauthorizedCacheControlHeaderStrategy: StrictStr | None = None
