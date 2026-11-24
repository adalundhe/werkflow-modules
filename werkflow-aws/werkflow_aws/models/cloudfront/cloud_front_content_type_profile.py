from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontContentTypeProfile(BaseModel):
    Format: StrictStr | None = None
    ProfileId: StrictStr | None = None
    ContentType: StrictStr | None = None
