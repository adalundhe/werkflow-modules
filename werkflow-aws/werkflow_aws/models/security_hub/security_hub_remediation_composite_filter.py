from __future__ import annotations
from pydantic import BaseModel
from .security_hub_remediation_string_filter import SecurityHubRemediationStringFilter


class SecurityHubRemediationCompositeFilter(BaseModel):
    StringFilters: list[SecurityHubRemediationStringFilter] | None = None
