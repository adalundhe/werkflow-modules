from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessImageSourceDetails(BaseModel):
    mediaId: StrictStr | None = None
    mediaMimeType: StrictStr | None = None
