from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_list_policies_granting_service_access_entry import IAMListPoliciesGrantingServiceAccessEntry


class IAMListPoliciesGrantingServiceAccessResponse(BaseModel):
    PoliciesGrantingServiceAccess: list[IAMListPoliciesGrantingServiceAccessEntry] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
