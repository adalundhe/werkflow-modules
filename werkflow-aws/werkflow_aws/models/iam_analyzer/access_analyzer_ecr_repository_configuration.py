from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerEcrRepositoryConfiguration(BaseModel):
    repositoryPolicy: StrictStr | None = None
