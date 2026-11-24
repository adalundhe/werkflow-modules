from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_resources_composite_filter import SecurityHubResourcesCompositeFilter


class SecurityHubResourcesFilters(BaseModel):
    CompositeFilters: list[SecurityHubResourcesCompositeFilter] | None = None
    CompositeOperator: StrictStr | None = None
