from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt, StrictStr
from .issue_bean import IssueBean
from .json_type_bean import JsonTypeBean


class SearchResults(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    expand: StrictStr | None = None
    issues: list[IssueBean] | None = None
    maxResults: StrictInt | None = None
    names: dict[StrictStr, StrictStr] | None = None
    schema_: dict[StrictStr, JsonTypeBean] | None = PydanticField(default=None, alias='schema')
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    warningMessages: list[StrictStr] | None = None
