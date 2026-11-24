from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStringConfigurationOptions(BaseModel):
    DefaultValue: StrictStr | None = None
    Re2Expression: StrictStr | None = None
    ExpressionDescription: StrictStr | None = None
