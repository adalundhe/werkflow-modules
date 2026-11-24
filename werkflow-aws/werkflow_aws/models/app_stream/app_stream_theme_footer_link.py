from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamThemeFooterLink(BaseModel):
    DisplayName: StrictStr | None = None
    FooterLinkURL: StrictStr | None = None
