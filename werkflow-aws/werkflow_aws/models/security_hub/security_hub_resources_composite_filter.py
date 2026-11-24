from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_resources_date_filter import SecurityHubResourcesDateFilter
from .security_hub_resources_map_filter import SecurityHubResourcesMapFilter
from .security_hub_resources_number_filter import SecurityHubResourcesNumberFilter
from .security_hub_resources_string_filter import SecurityHubResourcesStringFilter


class SecurityHubResourcesCompositeFilter(BaseModel):
    StringFilters: list[SecurityHubResourcesStringFilter] | None = None
    DateFilters: list[SecurityHubResourcesDateFilter] | None = None
    NumberFilters: list[SecurityHubResourcesNumberFilter] | None = None
    MapFilters: list[SecurityHubResourcesMapFilter] | None = None
    NestedCompositeFilters: list[SecurityHubResourcesCompositeFilter] | None = None
    Operator: StrictStr | None = None
