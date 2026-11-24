from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteRemediationConfigurationRequest(BaseModel):
    ConfigRuleName: StrictStr
    ResourceType: StrictStr | None = None
