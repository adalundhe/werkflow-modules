from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamUrlRedirectionConfig(BaseModel):
    Enabled: StrictBool | None = None
    AllowedUrls: list[StrictStr] | None = None
    DeniedUrls: list[StrictStr] | None = None
