from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueConnectionTypeVariant(BaseModel):
    ConnectionTypeVariantName: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    LogoUrl: StrictStr | None = None
