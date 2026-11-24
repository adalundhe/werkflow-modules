from __future__ import annotations
from pydantic import BaseModel
from .awss3_error_document_input import AWSS3ErrorDocumentInput
from .awss3_index_document_input import AWSS3IndexDocumentInput
from .awss3_redirect_all_requests_to_input import AWSS3RedirectAllRequestsToInput
from .awss3_routing_rule_input import AWSS3RoutingRuleInput


class AWSS3WebsiteConfiguration(BaseModel):
    ErrorDocument: AWSS3ErrorDocumentInput | None = None
    IndexDocument: AWSS3IndexDocumentInput | None = None
    RedirectAllRequestsTo: AWSS3RedirectAllRequestsToInput | None = None
    RoutingRules: list[AWSS3RoutingRuleInput] | None = None
