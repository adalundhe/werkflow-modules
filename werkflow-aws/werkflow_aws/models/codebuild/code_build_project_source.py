from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_build_build_status_config import CodeBuildBuildStatusConfig
from .code_build_git_submodules_config import CodeBuildGitSubmodulesConfig
from .code_build_source_auth import CodeBuildSourceAuth


class CodeBuildProjectSource(BaseModel):
    type: StrictStr | None = None
    location: StrictStr | None = None
    gitCloneDepth: StrictInt | None = None
    gitSubmodulesConfig: CodeBuildGitSubmodulesConfig | None = None
    buildspec: StrictStr | None = None
    auth: CodeBuildSourceAuth | None = None
    reportBuildStatus: StrictBool | None = None
    buildStatusConfig: CodeBuildBuildStatusConfig | None = None
    insecureSsl: StrictBool | None = None
    sourceIdentifier: StrictStr | None = None
