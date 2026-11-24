from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSRepositoryCredentials(BaseModel):
    credentialsParameter: StrictStr | None = None
