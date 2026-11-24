from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SuggestedIssue(BaseModel):
    id: StrictInt | None = None
    img: StrictStr | None = None
    key: StrictStr | None = None
    keyHtml: StrictStr | None = None
    summary: StrictStr | None = None
    summaryText: StrictStr | None = None
