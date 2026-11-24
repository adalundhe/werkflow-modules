from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_report_export_config import CodeBuildReportExportConfig
from .code_build_tag import CodeBuildTag


class CodeBuildUpdateReportGroupRequest(BaseModel):
    arn: StrictStr
    exportConfig: CodeBuildReportExportConfig | None = None
    tags: list[CodeBuildTag] | None = None
