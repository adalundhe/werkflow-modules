from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .code_guru_repository_analysis import CodeGuruRepositoryAnalysis


class CodeGuruCodeReviewType(BaseModel):
    RepositoryAnalysis: CodeGuruRepositoryAnalysis
    AnalysisTypes: list[Literal['Security', 'CodeQuality']] | None = None
