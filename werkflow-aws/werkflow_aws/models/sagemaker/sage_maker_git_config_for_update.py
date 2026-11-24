from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGitConfigForUpdate(BaseModel):
    SecretArn: StrictStr | None = None
