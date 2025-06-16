from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)


class OrganizationsListAccountsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None