from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .organizations_tag_model import OrganizationsTagModel


class OrganizationsCreateAccountRequest(BaseModel):
    Email: StrictStr
    AccountName: StrictStr
    RoleName: StrictStr | None = None
    IamUserAccessToBilling: Literal['ALLOW', 'DENY'] | None = None
    Tags: list[OrganizationsTagModel] | None = None
