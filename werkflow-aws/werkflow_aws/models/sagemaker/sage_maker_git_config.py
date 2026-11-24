from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGitConfig(BaseModel):
    RepositoryUrl: StrictStr | None = None
    Branch: StrictStr | None = None
    SecretArn: StrictStr | None = None
