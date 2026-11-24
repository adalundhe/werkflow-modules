from __future__ import annotations
from pydantic import BaseModel
from .code_guru_code_commit_repository import CodeGuruCodeCommitRepository
from .code_guru_s3_repository import CodeGuruS3Repository
from .code_guru_third_party_source_repository import CodeGuruThirdPartySourceRepository


class CodeGuruRepository(BaseModel):
    CodeCommit: CodeGuruCodeCommitRepository | None = None
    Bitbucket: CodeGuruThirdPartySourceRepository | None = None
    GitHubEnterpriseServer: CodeGuruThirdPartySourceRepository | None = None
    S3Bucket: CodeGuruS3Repository | None = None
