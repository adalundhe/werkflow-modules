from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .code_build_report_export_config import CodeBuildReportExportConfig
from .code_build_tag import CodeBuildTag


class CodeBuildCreateReportGroupRequest(BaseModel):
    name: StrictStr
    type: Literal['TEST', 'CODE_COVERAGE']
    exportConfig: CodeBuildReportExportConfig
    tags: list[CodeBuildTag] | None = None
