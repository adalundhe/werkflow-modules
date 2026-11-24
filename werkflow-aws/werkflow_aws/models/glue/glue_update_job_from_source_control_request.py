from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueUpdateJobFromSourceControlRequest(BaseModel):
    JobName: StrictStr | None = None
    Provider: Literal['GITHUB', 'GITLAB', 'BITBUCKET', 'AWS_CODE_COMMIT'] | None = None
    RepositoryName: StrictStr | None = None
    RepositoryOwner: StrictStr | None = None
    BranchName: StrictStr | None = None
    Folder: StrictStr | None = None
    CommitId: StrictStr | None = None
    AuthStrategy: Literal['PERSONAL_ACCESS_TOKEN', 'AWS_SECRETS_MANAGER'] | None = None
    AuthToken: StrictStr | None = None
