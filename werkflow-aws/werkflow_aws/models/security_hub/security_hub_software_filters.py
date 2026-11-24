from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_software_composite_filter import SecurityHubSoftwareCompositeFilter


class SecurityHubSoftwareFilters(BaseModel):
    CompositeFilters: list[SecurityHubSoftwareCompositeFilter] | None = None
    CompositeOperator: Literal['AND', 'OR'] | None = None
