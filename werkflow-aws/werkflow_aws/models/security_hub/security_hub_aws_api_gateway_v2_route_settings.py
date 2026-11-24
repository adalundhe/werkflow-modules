from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class SecurityHubAwsApiGatewayV2RouteSettings(BaseModel):
    DetailedMetricsEnabled: StrictBool | None = None
    LoggingLevel: StrictStr | None = None
    DataTraceEnabled: StrictBool | None = None
    ThrottlingBurstLimit: StrictInt | None = None
    ThrottlingRateLimit: StrictFloat | StrictInt | None = None
