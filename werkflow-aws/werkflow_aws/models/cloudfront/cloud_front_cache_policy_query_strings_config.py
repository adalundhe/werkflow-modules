from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_query_string_names import CloudFrontQueryStringNames


class CloudFrontCachePolicyQueryStringsConfig(BaseModel):
    QueryStringBehavior: StrictStr | None = None
    QueryStrings: CloudFrontQueryStringNames | None = None
