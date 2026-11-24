from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_email_address_search_criteria import ConnectEmailAddressSearchCriteria
from .connect_email_address_search_filter import ConnectEmailAddressSearchFilter


class ConnectSearchEmailAddressesRequest(BaseModel):
    InstanceId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SearchCriteria: ConnectEmailAddressSearchCriteria | None = None
    SearchFilter: ConnectEmailAddressSearchFilter | None = None
