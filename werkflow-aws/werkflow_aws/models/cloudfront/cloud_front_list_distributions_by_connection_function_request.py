from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListDistributionsByConnectionFunctionRequest(BaseModel):
    ConnectionFunctionIdentifier: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
