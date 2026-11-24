from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_application_theme import QuickSightApplicationTheme
from .quick_sight_logo_configuration import QuickSightLogoConfiguration


class QuickSightBrandDefinition(BaseModel):
    BrandName: StrictStr | None = None
    Description: StrictStr | None = None
    ApplicationTheme: QuickSightApplicationTheme | None = None
    LogoConfiguration: QuickSightLogoConfiguration | None = None
