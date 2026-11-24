from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .code_build_code_coverage_report_summary import CodeBuildCodeCoverageReportSummary
from .code_build_report_export_config import CodeBuildReportExportConfig
from .code_build_test_report_summary import CodeBuildTestReportSummary


class CodeBuildReport(BaseModel):
    arn: StrictStr | None = None
    type: StrictStr | None = None
    name: StrictStr | None = None
    reportGroupArn: StrictStr | None = None
    executionId: StrictStr | None = None
    status: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    expired: datetime.datetime | StrictStr | None = None
    exportConfig: CodeBuildReportExportConfig | None = None
    truncated: StrictBool | None = None
    testSummary: CodeBuildTestReportSummary | None = None
    codeCoverageSummary: CodeBuildCodeCoverageReportSummary | None = None
