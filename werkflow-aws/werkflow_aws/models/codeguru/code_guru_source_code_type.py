from __future__ import annotations
from pydantic import BaseModel
from .code_guru_branch_diff_source_code_type import CodeGuruBranchDiffSourceCodeType
from .code_guru_commit_diff_source_code_type import CodeGuruCommitDiffSourceCodeType
from .code_guru_repository_head_source_code_type import CodeGuruRepositoryHeadSourceCodeType
from .code_guru_request_metadata import CodeGuruRequestMetadata
from .code_guru_s3_bucket_repository import CodeGuruS3BucketRepository


class CodeGuruSourceCodeType(BaseModel):
    CommitDiff: CodeGuruCommitDiffSourceCodeType | None = None
    RepositoryHead: CodeGuruRepositoryHeadSourceCodeType | None = None
    BranchDiff: CodeGuruBranchDiffSourceCodeType | None = None
    S3BucketRepository: CodeGuruS3BucketRepository | None = None
    RequestMetadata: CodeGuruRequestMetadata | None = None
