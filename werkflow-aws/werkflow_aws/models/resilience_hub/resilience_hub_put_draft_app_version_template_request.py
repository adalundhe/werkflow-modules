from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubPutDraftAppVersionTemplateRequest(BaseModel):
    appArn: StrictStr
    appTemplateBody: StrictStr
