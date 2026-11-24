from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateParallelDataDataLocation(BaseModel):
    RepositoryType: StrictStr | None = None
    Location: StrictStr | None = None
