from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessQuickSightConfiguration(BaseModel):
    clientNamespace: StrictStr | None = None
