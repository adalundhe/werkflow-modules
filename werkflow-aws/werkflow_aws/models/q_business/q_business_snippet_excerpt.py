from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessSnippetExcerpt(BaseModel):
    text: StrictStr | None = None
