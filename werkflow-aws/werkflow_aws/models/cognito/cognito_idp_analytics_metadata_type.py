from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAnalyticsMetadataType(BaseModel):
    AnalyticsEndpointId: StrictStr | None = None
