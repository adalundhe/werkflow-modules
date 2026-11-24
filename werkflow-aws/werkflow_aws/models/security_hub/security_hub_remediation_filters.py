from __future__ import annotations
from pydantic import BaseModel
from .security_hub_remediation_composite_filter import SecurityHubRemediationCompositeFilter


class SecurityHubRemediationFilters(BaseModel):
    CompositeFilters: list[SecurityHubRemediationCompositeFilter] | None = None
