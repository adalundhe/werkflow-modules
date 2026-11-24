from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_theme_footer_link import AppStreamThemeFooterLink


class AppStreamCreateThemeForStackRequest(BaseModel):
    StackName: StrictStr
    TitleText: StrictStr
    ThemeStyling: Literal['LIGHT_BLUE', 'BLUE', 'PINK', 'RED']
    OrganizationLogoS3Location: AppStreamS3Location
    FaviconS3Location: AppStreamS3Location
    FooterLinks: list[AppStreamThemeFooterLink] | None = None
