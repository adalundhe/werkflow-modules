from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSElasticsearchSettings(BaseModel):
    ServiceAccessRoleArn: StrictStr | None = None
    EndpointUri: StrictStr | None = None
    FullLoadErrorPercentage: StrictInt | None = None
    ErrorRetryDuration: StrictInt | None = None
    UseNewMappingType: StrictBool | None = None
