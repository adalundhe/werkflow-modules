from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUserInfo(BaseModel):
    name: StrictStr | None = None
    email: StrictStr | None = None
    date: StrictStr | None = None
