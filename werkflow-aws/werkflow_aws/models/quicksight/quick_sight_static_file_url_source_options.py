from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStaticFileUrlSourceOptions(BaseModel):
    Url: StrictStr | None = None
