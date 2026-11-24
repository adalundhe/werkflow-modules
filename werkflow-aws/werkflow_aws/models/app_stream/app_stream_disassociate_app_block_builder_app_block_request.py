from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDisassociateAppBlockBuilderAppBlockRequest(BaseModel):
    AppBlockArn: StrictStr
    AppBlockBuilderName: StrictStr
