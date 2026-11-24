from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RuleConfiguration(BaseModel):
    disabled: StrictBool | None = None
    tag: StrictStr | None = None
    value: StrictStr | None = None
