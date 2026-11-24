from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateTerminologyDataLocation(BaseModel):
    RepositoryType: StrictStr | None = None
    Location: StrictStr | None = None
