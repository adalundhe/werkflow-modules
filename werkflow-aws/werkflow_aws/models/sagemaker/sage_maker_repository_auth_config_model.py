from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRepositoryAuthConfigModel(BaseModel):
    RepositoryCredentialsProviderArn: StrictStr | None = None
