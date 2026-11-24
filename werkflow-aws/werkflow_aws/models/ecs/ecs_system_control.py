from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSSystemControl(BaseModel):
    namespace: StrictStr | None = None
    value: StrictStr | None = None
