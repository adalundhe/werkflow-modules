from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_repository_access_mode import SageMakerRepositoryAccessMode
from .sage_maker_repository_auth_config import SageMakerRepositoryAuthConfig


class SageMakerImageConfig(BaseModel):
    RepositoryAccessMode: SageMakerRepositoryAccessMode | None = None
    RepositoryAuthConfig: SageMakerRepositoryAuthConfig | None = None
