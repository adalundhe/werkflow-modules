from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsWafv2CustomHttpHeader(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
