from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_error_document import AWSS3ErrorDocument
from .awss3_index_document import AWSS3IndexDocument
from .awss3_redirect_all_requests_to import AWSS3RedirectAllRequestsTo
from .awss3_routing_rule import AWSS3RoutingRule


class AWSS3GetBucketWebsiteResponse(BaseModel):
    RedirectAllRequestsTo: AWSS3RedirectAllRequestsTo | None = None
    IndexDocument: AWSS3IndexDocument | None = None
    ErrorDocument: AWSS3ErrorDocument | None = None
    RoutingRules: list[AWSS3RoutingRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
