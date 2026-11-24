from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_table_field_link_content_configuration import QuickSightTableFieldLinkContentConfiguration


class QuickSightTableFieldLinkConfiguration(BaseModel):
    Target: StrictStr | None = None
    Content: QuickSightTableFieldLinkContentConfiguration | None = None
