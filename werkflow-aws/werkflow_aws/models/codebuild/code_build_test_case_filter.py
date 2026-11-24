from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildTestCaseFilter(BaseModel):
    status: StrictStr | None = None
    keyword: StrictStr | None = None
