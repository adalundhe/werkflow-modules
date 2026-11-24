from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_default_interactive_layout_configuration import QuickSightDefaultInteractiveLayoutConfiguration
from .quick_sight_default_paginated_layout_configuration import QuickSightDefaultPaginatedLayoutConfiguration


class QuickSightDefaultNewSheetConfiguration(BaseModel):
    InteractiveLayoutConfiguration: QuickSightDefaultInteractiveLayoutConfiguration | None = None
    PaginatedLayoutConfiguration: QuickSightDefaultPaginatedLayoutConfiguration | None = None
    SheetContentType: StrictStr | None = None
