from __future__ import annotations
from pydantic import BaseModel
from .security_hub_cell import SecurityHubCell
from .security_hub_page import SecurityHubPage
from .security_hub_range import SecurityHubRange
from .security_hub_record import SecurityHubRecord


class SecurityHubOccurrences(BaseModel):
    LineRanges: list[SecurityHubRange] | None = None
    OffsetRanges: list[SecurityHubRange] | None = None
    Pages: list[SecurityHubPage] | None = None
    Records: list[SecurityHubRecord] | None = None
    Cells: list[SecurityHubCell] | None = None
