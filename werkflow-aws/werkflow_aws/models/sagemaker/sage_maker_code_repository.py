from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCodeRepository(BaseModel):
    RepositoryUrl: StrictStr | None = None
