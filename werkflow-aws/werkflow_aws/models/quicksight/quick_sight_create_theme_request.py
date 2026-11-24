from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission
from .quick_sight_tag import QuickSightTag
from .quick_sight_theme_configuration import QuickSightThemeConfiguration


class QuickSightCreateThemeRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    Name: StrictStr
    BaseThemeId: StrictStr
    Configuration: QuickSightThemeConfiguration
    VersionDescription: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    Tags: list[QuickSightTag] | None = None
