from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ClientLoginBannerResponseOptions(BaseModel):
    Enabled: StrictBool | None = None
    BannerText: StrictStr | None = None
