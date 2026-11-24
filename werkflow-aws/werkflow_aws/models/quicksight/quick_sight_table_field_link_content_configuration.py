from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_field_custom_icon_content import QuickSightTableFieldCustomIconContent
from .quick_sight_table_field_custom_text_content import QuickSightTableFieldCustomTextContent


class QuickSightTableFieldLinkContentConfiguration(BaseModel):
    CustomTextContent: QuickSightTableFieldCustomTextContent | None = None
    CustomIconContent: QuickSightTableFieldCustomIconContent | None = None
