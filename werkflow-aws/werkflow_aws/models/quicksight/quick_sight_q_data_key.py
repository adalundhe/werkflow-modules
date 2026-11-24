from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQDataKey(BaseModel):
    QDataKeyArn: StrictStr | None = None
    QDataKeyType: StrictStr | None = None
