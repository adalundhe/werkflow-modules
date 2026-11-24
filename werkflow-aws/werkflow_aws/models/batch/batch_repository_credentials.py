from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchRepositoryCredentials(BaseModel):
    credentialsParameter: StrictStr | None = None
