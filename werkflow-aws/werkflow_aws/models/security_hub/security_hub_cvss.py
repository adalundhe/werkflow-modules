from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .security_hub_adjustment import SecurityHubAdjustment


class SecurityHubCvss(BaseModel):
    Version: StrictStr | None = None
    BaseScore: StrictFloat | StrictInt | None = None
    BaseVector: StrictStr | None = None
    Source: StrictStr | None = None
    Adjustments: list[SecurityHubAdjustment] | None = None
