from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStartImageBuilderRequest(BaseModel):
    Name: StrictStr
    AppstreamAgentVersion: StrictStr | None = None
