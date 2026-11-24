from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_git_pull_request_filter import CodePipelineGitPullRequestFilter
from .code_pipeline_git_push_filter import CodePipelineGitPushFilter


class CodePipelineGitConfiguration(BaseModel):
    sourceActionName: StrictStr | None = None
    push: list[CodePipelineGitPushFilter] | None = None
    pullRequest: list[CodePipelineGitPullRequestFilter] | None = None
