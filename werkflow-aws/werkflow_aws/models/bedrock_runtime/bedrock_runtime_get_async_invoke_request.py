from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGetAsyncInvokeRequest(BaseModel):
    invocationArn: StrictStr
