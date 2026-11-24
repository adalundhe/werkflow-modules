from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ClientLoginBannerOptions(BaseModel):
    Enabled: StrictBool | None = None
    BannerText: StrictStr | None = None
