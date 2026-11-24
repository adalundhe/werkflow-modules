from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowApiKeyCredentials(BaseModel):
    apiKey: StrictStr
    apiSecretKey: StrictStr | None = None
