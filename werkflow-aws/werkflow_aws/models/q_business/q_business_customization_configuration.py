from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessCustomizationConfiguration(BaseModel):
    customCSSUrl: StrictStr | None = None
    logoUrl: StrictStr | None = None
    fontUrl: StrictStr | None = None
    faviconUrl: StrictStr | None = None
