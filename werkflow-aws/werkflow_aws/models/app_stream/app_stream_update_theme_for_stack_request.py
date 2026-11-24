from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_theme_footer_link import AppStreamThemeFooterLink


class AppStreamUpdateThemeForStackRequest(BaseModel):
    StackName: StrictStr
    FooterLinks: list[AppStreamThemeFooterLink] | None = None
    TitleText: StrictStr | None = None
    ThemeStyling: Literal['LIGHT_BLUE', 'BLUE', 'PINK', 'RED'] | None = None
    OrganizationLogoS3Location: AppStreamS3Location | None = None
    FaviconS3Location: AppStreamS3Location | None = None
    State: Literal['ENABLED', 'DISABLED'] | None = None
    AttributesToDelete: list[Literal['FOOTER_LINKS']] | None = None
