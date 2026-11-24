from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_git_branch_filter_criteria import CodePipelineGitBranchFilterCriteria
from .code_pipeline_git_file_path_filter_criteria import CodePipelineGitFilePathFilterCriteria
from .code_pipeline_git_tag_filter_criteria import CodePipelineGitTagFilterCriteria


class CodePipelineGitPushFilter(BaseModel):
    tags: CodePipelineGitTagFilterCriteria | None = None
    branches: CodePipelineGitBranchFilterCriteria | None = None
    filePaths: CodePipelineGitFilePathFilterCriteria | None = None
