from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendErrorsListItem(BaseModel):
    Page: StrictInt | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
