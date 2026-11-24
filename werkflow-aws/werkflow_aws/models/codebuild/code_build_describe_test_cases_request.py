from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_test_case_filter import CodeBuildTestCaseFilter


class CodeBuildDescribeTestCasesRequest(BaseModel):
    reportArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: CodeBuildTestCaseFilter | None = None
