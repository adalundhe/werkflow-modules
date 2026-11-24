from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyWafConfiguration(BaseModel):
    webAclArn: StrictStr | None = None
    wafStatus: StrictStr | None = None
    statusReason: StrictStr | None = None
