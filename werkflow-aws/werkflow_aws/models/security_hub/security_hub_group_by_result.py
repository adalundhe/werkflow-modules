from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_group_by_value import SecurityHubGroupByValue


class SecurityHubGroupByResult(BaseModel):
    GroupByField: StrictStr | None = None
    GroupByValues: list[SecurityHubGroupByValue] | None = None
