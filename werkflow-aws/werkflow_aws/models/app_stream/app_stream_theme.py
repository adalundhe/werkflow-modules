from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_theme_footer_link import AppStreamThemeFooterLink


class AppStreamTheme(BaseModel):
    StackName: StrictStr | None = None
    State: StrictStr | None = None
    ThemeTitleText: StrictStr | None = None
    ThemeStyling: StrictStr | None = None
    ThemeFooterLinks: list[AppStreamThemeFooterLink] | None = None
    ThemeOrganizationLogoURL: StrictStr | None = None
    ThemeFaviconURL: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
