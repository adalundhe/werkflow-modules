from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeDraftAppVersionResourcesImportStatusRequest(BaseModel):
    appArn: StrictStr
