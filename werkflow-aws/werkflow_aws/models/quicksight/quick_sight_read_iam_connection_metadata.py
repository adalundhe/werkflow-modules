from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReadIamConnectionMetadata(BaseModel):
    RoleArn: StrictStr | None = None
    SourceArn: StrictStr | None = None
