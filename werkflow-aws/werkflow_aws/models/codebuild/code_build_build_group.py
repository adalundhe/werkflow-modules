from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .code_build_build_summary import CodeBuildBuildSummary


class CodeBuildBuildGroup(BaseModel):
    identifier: StrictStr | None = None
    dependsOn: list[StrictStr] | None = None
    ignoreFailure: StrictBool | None = None
    currentBuildSummary: CodeBuildBuildSummary | None = None
    priorBuildSummaryList: list[CodeBuildBuildSummary] | None = None
