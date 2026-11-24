from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESTrackingOptions(BaseModel):
    CustomRedirectDomain: StrictStr | None = None
    HttpsPolicy: StrictStr | None = None
