from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAssociateAppBlockBuilderAppBlockRequest(BaseModel):
    AppBlockArn: StrictStr
    AppBlockBuilderName: StrictStr
