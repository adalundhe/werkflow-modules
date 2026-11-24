from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_theme_configuration import QuickSightThemeConfiguration
from .quick_sight_theme_error import QuickSightThemeError


class QuickSightThemeVersion(BaseModel):
    VersionNumber: StrictInt | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    BaseThemeId: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Configuration: QuickSightThemeConfiguration | None = None
    Errors: list[QuickSightThemeError] | None = None
    Status: StrictStr | None = None
