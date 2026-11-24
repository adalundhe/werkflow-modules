from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceGetCustomRulePolicyRequest(BaseModel):
    ConfigRuleName: StrictStr | None = None
