from pydantic import (
    BaseModel,
    StrictStr
)

from .organizations_account import OrganizationsAccount


class OrganizationsListAccountsResponse(BaseModel):
    Accounts: list[OrganizationsAccount]
    NextToken: StrictStr | None = None