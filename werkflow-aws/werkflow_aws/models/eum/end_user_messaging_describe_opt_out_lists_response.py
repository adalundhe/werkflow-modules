from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_opt_out_list_information import EndUserMessagingOptOutListInformation


class EndUserMessagingDescribeOptOutListsResponse(BaseModel):
    OptOutLists: list[EndUserMessagingOptOutListInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
