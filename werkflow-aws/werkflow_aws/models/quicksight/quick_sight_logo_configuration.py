from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_logo_set_configuration import QuickSightLogoSetConfiguration


class QuickSightLogoConfiguration(BaseModel):
    AltText: StrictStr | None = None
    LogoSet: QuickSightLogoSetConfiguration | None = None
