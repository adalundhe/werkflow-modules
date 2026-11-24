from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailDistributionCustomErrorResponse(BaseModel):
    errorCode: StrictInt | None = None
    responseCode: StrictStr | None = None
    responsePagePath: StrictStr | None = None
    errorCachingMinTTL: StrictInt | None = None
