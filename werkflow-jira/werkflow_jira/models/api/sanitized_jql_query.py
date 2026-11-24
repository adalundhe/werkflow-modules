from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .error_collection import ErrorCollection


class SanitizedJqlQuery(BaseModel):
    accountId: StrictStr | None = None
    errors: ErrorCollection | None = None
    initialQuery: StrictStr | None = None
    sanitizedQuery: StrictStr | None = None
