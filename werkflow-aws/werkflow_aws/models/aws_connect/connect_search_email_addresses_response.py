from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_email_address_metadata import ConnectEmailAddressMetadata


class ConnectSearchEmailAddressesResponse(BaseModel):
    NextToken: StrictStr | None = None
    EmailAddresses: list[ConnectEmailAddressMetadata] | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
