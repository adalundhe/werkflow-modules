from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAllowedExtension(BaseModel):
    Extension: StrictStr | None = None
