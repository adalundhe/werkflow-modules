from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubKbArticle(BaseModel):
    Title: StrictStr | None = None
    Url: StrictStr | None = None
