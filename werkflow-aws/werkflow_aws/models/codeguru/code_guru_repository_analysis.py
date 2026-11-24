from __future__ import annotations
from pydantic import BaseModel
from .code_guru_repository_head_source_code_type import CodeGuruRepositoryHeadSourceCodeType
from .code_guru_source_code_type import CodeGuruSourceCodeType


class CodeGuruRepositoryAnalysis(BaseModel):
    RepositoryHead: CodeGuruRepositoryHeadSourceCodeType | None = None
    SourceCodeType: CodeGuruSourceCodeType | None = None
