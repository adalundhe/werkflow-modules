from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubStringListConfigurationOptions(BaseModel):
    DefaultValue: list[StrictStr] | None = None
    Re2Expression: StrictStr | None = None
    MaxItems: StrictInt | None = None
    ExpressionDescription: StrictStr | None = None
