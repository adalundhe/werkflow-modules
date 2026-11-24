from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESArchivingOptions(BaseModel):
    ArchiveArn: StrictStr | None = None
