from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessKendraIndexConfiguration(BaseModel):
    indexId: StrictStr | None = None
