from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_s3_report_export_config import CodeBuildS3ReportExportConfig


class CodeBuildReportExportConfig(BaseModel):
    exportConfigType: StrictStr | None = None
    s3Destination: CodeBuildS3ReportExportConfig | None = None
