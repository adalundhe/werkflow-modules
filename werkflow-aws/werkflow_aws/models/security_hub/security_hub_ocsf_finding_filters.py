from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_composite_filter import SecurityHubCompositeFilter


class SecurityHubOcsfFindingFilters(BaseModel):
    CompositeFilters: list[SecurityHubCompositeFilter] | None = None
    CompositeOperator: StrictStr | None = None
