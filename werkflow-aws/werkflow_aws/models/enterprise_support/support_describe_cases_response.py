from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .support_case_details import SupportCaseDetails


class SupportDescribeCasesResponse(BaseModel):
    cases: list[SupportCaseDetails] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
