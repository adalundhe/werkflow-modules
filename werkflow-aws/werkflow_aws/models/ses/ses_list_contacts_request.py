from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ses_list_contacts_filter import SESListContactsFilter


class SESListContactsRequest(BaseModel):
    ContactListName: StrictStr
    Filter: SESListContactsFilter | None = None
    PageSize: StrictInt | None = None
    NextToken: StrictStr | None = None
