from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_build_report_export_config import CodeBuildReportExportConfig
from .code_build_tag import CodeBuildTag


class CodeBuildReportGroup(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    exportConfig: CodeBuildReportExportConfig | None = None
    created: datetime.datetime | StrictStr | None = None
    lastModified: datetime.datetime | StrictStr | None = None
    tags: list[CodeBuildTag] | None = None
    status: StrictStr | None = None
