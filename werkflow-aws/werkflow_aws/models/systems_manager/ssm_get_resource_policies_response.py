from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_get_resource_policies_response_entry import SSMGetResourcePoliciesResponseEntry


class SSMGetResourcePoliciesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Policies: list[SSMGetResourcePoliciesResponseEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
