from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontValidationTokenDetail(BaseModel):
    Domain: StrictStr | None = None
    RedirectTo: StrictStr | None = None
    RedirectFrom: StrictStr | None = None
