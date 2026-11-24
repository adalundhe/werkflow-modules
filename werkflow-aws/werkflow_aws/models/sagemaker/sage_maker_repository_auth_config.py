from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRepositoryAuthConfig(BaseModel):
    RepositoryCredentialsProviderArn: StrictStr | None = None
