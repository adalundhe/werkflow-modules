from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_opted_out_number_information import EndUserMessagingOptedOutNumberInformation


class EndUserMessagingDescribeOptedOutNumbersResponse(BaseModel):
    OptOutListArn: StrictStr | None = None
    OptOutListName: StrictStr | None = None
    OptedOutNumbers: list[EndUserMessagingOptedOutNumberInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
