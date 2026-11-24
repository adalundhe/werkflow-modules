from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_git_configuration import CodePipelineGitConfiguration


class CodePipelinePipelineTriggerDeclaration(BaseModel):
    providerType: StrictStr | None = None
    gitConfiguration: CodePipelineGitConfiguration | None = None
