from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_git_config import SageMakerGitConfig


class SageMakerDescribeCodeRepositoryResponse(BaseModel):
    CodeRepositoryName: StrictStr | None = None
    CodeRepositoryArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    GitConfig: SageMakerGitConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
