from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictBool, StrictStr
from .issue_bean import IssueBean
from .json_type_bean import JsonTypeBean
from .search_warning import SearchWarning


class SearchAndReconcileResults(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    isLast: StrictBool | None = None
    issues: list[IssueBean] | None = None
    names: dict[StrictStr, StrictStr] | None = None
    nextPageToken: StrictStr | None = None
    schema_: dict[StrictStr, JsonTypeBean] | None = PydanticField(default=None, alias='schema')
    warnings: list[SearchWarning] | None = None
