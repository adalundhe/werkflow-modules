from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DetectiveNewUserAgentDetail(BaseModel):
    UserAgent: StrictStr | None = None
    IsNewForEntireAccount: StrictBool | None = None
