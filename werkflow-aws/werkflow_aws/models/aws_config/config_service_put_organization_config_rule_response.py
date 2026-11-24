from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConfigServicePutOrganizationConfigRuleResponse(BaseModel):
    OrganizationConfigRuleArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
