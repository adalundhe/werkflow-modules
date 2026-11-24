from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_document import OpenSearchServerlessDocument


class OpenSearchServerlessLifecyclePolicyDetail(BaseModel):
    type: StrictStr | None = None
    name: StrictStr | None = None
    policyVersion: StrictStr | None = None
    description: StrictStr | None = None
    policy: OpenSearchServerlessDocument | None = None
    createdDate: StrictInt | None = None
    lastModifiedDate: StrictInt | None = None
