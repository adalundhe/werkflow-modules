from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_git_config_for_update import SageMakerGitConfigForUpdate


class SageMakerUpdateCodeRepositoryRequest(BaseModel):
    CodeRepositoryName: StrictStr
    GitConfig: SageMakerGitConfigForUpdate | None = None
