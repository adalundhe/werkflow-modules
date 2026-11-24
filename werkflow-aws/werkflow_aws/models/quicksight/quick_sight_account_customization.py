from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAccountCustomization(BaseModel):
    DefaultTheme: StrictStr | None = None
    DefaultEmailCustomizationTemplate: StrictStr | None = None
