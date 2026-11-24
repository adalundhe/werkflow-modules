from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_logo_set import QuickSightLogoSet


class QuickSightLogo(BaseModel):
    AltText: StrictStr | None = None
    LogoSet: QuickSightLogoSet | None = None
