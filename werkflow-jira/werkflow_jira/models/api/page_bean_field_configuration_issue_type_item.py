from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .field_configuration_issue_type_item import FieldConfigurationIssueTypeItem


class PageBeanFieldConfigurationIssueTypeItem(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[FieldConfigurationIssueTypeItem] | None = None
