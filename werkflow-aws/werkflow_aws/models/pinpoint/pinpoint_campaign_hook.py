from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointCampaignHook(BaseModel):
    LambdaFunctionName: StrictStr | None = None
    Mode: StrictStr | None = None
    WebUrl: StrictStr | None = None
