from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RuleOption(BaseModel):
    Keyword: StrictStr | None = None
    Settings: list[StrictStr] | None = None
