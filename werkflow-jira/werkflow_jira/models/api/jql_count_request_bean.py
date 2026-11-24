from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JQLCountRequestBean(BaseModel):
    jql: StrictStr | None = None
