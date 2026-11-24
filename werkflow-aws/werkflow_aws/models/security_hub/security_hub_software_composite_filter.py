from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_software_string_filter import SecurityHubSoftwareStringFilter


class SecurityHubSoftwareCompositeFilter(BaseModel):
    StringFilters: list[SecurityHubSoftwareStringFilter] | None = None
    NestedCompositeFilters: list[SecurityHubSoftwareCompositeFilter] | None = None
    Operator: Literal['AND', 'OR'] | None = None
