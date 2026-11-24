from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AnnouncementBannerConfigurationUpdate(BaseModel):
    isDismissible: StrictBool | None = None
    isEnabled: StrictBool | None = None
    message: StrictStr | None = None
    visibility: StrictStr | None = None
