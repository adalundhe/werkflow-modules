from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMHttpRedirect(BaseModel):
    RedirectFrom: StrictStr | None = None
    RedirectTo: StrictStr | None = None
