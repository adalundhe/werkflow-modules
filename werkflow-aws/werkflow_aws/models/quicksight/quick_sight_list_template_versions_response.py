from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_template_version_summary import QuickSightTemplateVersionSummary


class QuickSightListTemplateVersionsResponse(BaseModel):
    TemplateVersionSummaryList: list[QuickSightTemplateVersionSummary] | None = None
    NextToken: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
