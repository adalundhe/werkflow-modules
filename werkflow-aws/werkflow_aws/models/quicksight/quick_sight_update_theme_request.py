from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_theme_configuration import QuickSightThemeConfiguration


class QuickSightUpdateThemeRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    BaseThemeId: StrictStr
    Name: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    Configuration: QuickSightThemeConfiguration | None = None
