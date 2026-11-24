from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendWarningsListItem(BaseModel):
    Page: StrictInt | None = None
    WarnCode: StrictStr | None = None
    WarnMessage: StrictStr | None = None
