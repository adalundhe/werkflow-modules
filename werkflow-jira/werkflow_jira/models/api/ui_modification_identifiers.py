from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UiModificationIdentifiers(BaseModel):
    id: StrictStr | None = None
    self: StrictStr | None = None
