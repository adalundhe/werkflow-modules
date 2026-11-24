from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteWebAppRequest(BaseModel):
    WebAppId: StrictStr
