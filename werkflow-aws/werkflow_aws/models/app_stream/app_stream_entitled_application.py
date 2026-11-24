from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamEntitledApplication(BaseModel):
    ApplicationIdentifier: StrictStr | None = None
