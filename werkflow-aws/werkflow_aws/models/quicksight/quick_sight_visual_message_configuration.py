from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightVisualMessageConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    Title: StrictStr | None = None
    TitleVisibility: StrictStr | None = None
    Description: StrictStr | None = None
    DescriptionVisibility: StrictStr | None = None
    LinkText: StrictStr | None = None
    LinkUrl: StrictStr | None = None
    LinkVisibility: StrictStr | None = None
