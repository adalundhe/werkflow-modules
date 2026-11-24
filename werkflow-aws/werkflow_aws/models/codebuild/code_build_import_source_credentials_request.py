from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildImportSourceCredentialsRequest(BaseModel):
    token: StrictStr
    serverType: Literal['GITHUB', 'BITBUCKET', 'GITHUB_ENTERPRISE', 'GITLAB', 'GITLAB_SELF_MANAGED']
    authType: Literal['OAUTH', 'BASIC_AUTH', 'PERSONAL_ACCESS_TOKEN', 'CODECONNECTIONS', 'SECRETS_MANAGER']
    username: StrictStr | None = None
    shouldOverwrite: StrictBool | None = None
