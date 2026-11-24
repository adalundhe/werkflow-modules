from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_verified_destination_number_information import EndUserMessagingVerifiedDestinationNumberInformation


class EndUserMessagingDescribeVerifiedDestinationNumbersResponse(BaseModel):
    VerifiedDestinationNumbers: list[EndUserMessagingVerifiedDestinationNumberInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
