from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_git_config import SageMakerGitConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateCodeRepositoryRequest(BaseModel):
    CodeRepositoryName: StrictStr
    GitConfig: SageMakerGitConfig
    Tags: list[SageMakerTagModel] | None = None
