from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_tag_model import OrganizationsTagModel


class OrganizationsPutResourcePolicyRequest(BaseModel):
    Content: StrictStr
    Tags: list[OrganizationsTagModel] | None = None
