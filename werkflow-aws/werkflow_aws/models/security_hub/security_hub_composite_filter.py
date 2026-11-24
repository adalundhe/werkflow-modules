from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_ocsf_boolean_filter import SecurityHubOcsfBooleanFilter
from .security_hub_ocsf_date_filter import SecurityHubOcsfDateFilter
from .security_hub_ocsf_ip_filter import SecurityHubOcsfIpFilter
from .security_hub_ocsf_map_filter import SecurityHubOcsfMapFilter
from .security_hub_ocsf_number_filter import SecurityHubOcsfNumberFilter
from .security_hub_ocsf_string_filter import SecurityHubOcsfStringFilter


class SecurityHubCompositeFilter(BaseModel):
    StringFilters: list[SecurityHubOcsfStringFilter] | None = None
    DateFilters: list[SecurityHubOcsfDateFilter] | None = None
    BooleanFilters: list[SecurityHubOcsfBooleanFilter] | None = None
    NumberFilters: list[SecurityHubOcsfNumberFilter] | None = None
    MapFilters: list[SecurityHubOcsfMapFilter] | None = None
    IpFilters: list[SecurityHubOcsfIpFilter] | None = None
    NestedCompositeFilters: list[SecurityHubCompositeFilter] | None = None
    Operator: StrictStr | None = None
