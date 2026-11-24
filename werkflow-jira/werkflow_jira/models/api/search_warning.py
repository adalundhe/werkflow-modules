from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .search_warning_limit_details import SearchWarningLimitDetails


class SearchWarning(BaseModel):
    details: SearchWarningLimitDetails | None = None
    message: StrictStr | None = None
    type: StrictStr | None = None
