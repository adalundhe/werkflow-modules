from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AnnouncementBannerConfiguration(BaseModel):
    hashId: StrictStr | None = None
    isDismissible: StrictBool | None = None
    isEnabled: StrictBool | None = None
    message: StrictStr | None = None
    visibility: StrictStr | None = None
