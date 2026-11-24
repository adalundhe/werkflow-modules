from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_category_diff_result import OpenSearchCategoryDiffResult


class OpenSearchCompareDomainConfigurationResponse(BaseModel):
    SourceDomainArn: StrictStr | None = None
    TargetDomainArn: StrictStr | None = None
    Categories: dict[StrictStr, OpenSearchCategoryDiffResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
