from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class APIGatewayV2RouteSettings(BaseModel):
    DataTraceEnabled: StrictBool | None = None
    DetailedMetricsEnabled: StrictBool | None = None
    LoggingLevel: StrictStr | None = None
    ThrottlingBurstLimit: StrictInt | None = None
    ThrottlingRateLimit: StrictFloat | StrictInt | None = None
