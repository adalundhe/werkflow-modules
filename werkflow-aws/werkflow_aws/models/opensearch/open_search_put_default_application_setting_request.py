from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchPutDefaultApplicationSettingRequest(BaseModel):
    applicationArn: StrictStr
    setAsDefault: StrictBool
