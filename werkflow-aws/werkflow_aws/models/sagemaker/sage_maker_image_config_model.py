from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_repository_auth_config_model import SageMakerRepositoryAuthConfigModel


class SageMakerImageConfigModel(BaseModel):
    RepositoryAccessMode: StrictStr | None = None
    RepositoryAuthConfig: SageMakerRepositoryAuthConfigModel | None = None
