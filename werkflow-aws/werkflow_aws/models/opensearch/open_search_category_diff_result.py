from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .open_search_diff_items import OpenSearchDiffItems


class OpenSearchCategoryDiffResult(BaseModel):
    Status: StrictStr | None = None
    InSync: StrictInt | None = None
    SourceOnly: StrictInt | None = None
    TargetOnly: StrictInt | None = None
    Diverged: StrictInt | None = None
    Items: OpenSearchDiffItems | None = None
    Truncated: StrictBool | None = None
