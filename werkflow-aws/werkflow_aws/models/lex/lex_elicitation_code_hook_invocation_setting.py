from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexElicitationCodeHookInvocationSetting(BaseModel):
    enableCodeHookInvocation: StrictBool | None = None
    invocationLabel: StrictStr | None = None
