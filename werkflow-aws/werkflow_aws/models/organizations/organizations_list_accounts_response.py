from pydantic import (
    BaseModel,
    StrictStr
)

from .organizations_account import OrganizationsAccount


class OrganizationsListAccountsResponse(BaseModel):
    Accounts: list[OrganizationsAccount] | None = None
    NextToken: StrictStr | None = None
