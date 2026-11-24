from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_git_branch_filter_criteria import CodePipelineGitBranchFilterCriteria
from .code_pipeline_git_file_path_filter_criteria import CodePipelineGitFilePathFilterCriteria


class CodePipelineGitPullRequestFilter(BaseModel):
    events: list[StrictStr] | None = None
    branches: CodePipelineGitBranchFilterCriteria | None = None
    filePaths: CodePipelineGitFilePathFilterCriteria | None = None
