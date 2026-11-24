from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_theme_version import QuickSightThemeVersion


class QuickSightTheme(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    ThemeId: StrictStr | None = None
    Version: QuickSightThemeVersion | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
