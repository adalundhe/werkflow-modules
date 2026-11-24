from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_describe_packages_filter import OpenSearchDescribePackagesFilter


class OpenSearchDescribePackagesRequest(BaseModel):
    Filters: list[OpenSearchDescribePackagesFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
