from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_verified_destination_number_filter import EndUserMessagingVerifiedDestinationNumberFilter


class EndUserMessagingDescribeVerifiedDestinationNumbersRequest(BaseModel):
    VerifiedDestinationNumberIds: list[StrictStr] | None = None
    DestinationPhoneNumbers: list[StrictStr] | None = None
    Filters: list[EndUserMessagingVerifiedDestinationNumberFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
