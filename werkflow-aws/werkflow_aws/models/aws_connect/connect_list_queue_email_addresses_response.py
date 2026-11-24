from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_email_address_summary import ConnectEmailAddressSummary


class ConnectListQueueEmailAddressesResponse(BaseModel):
    NextToken: StrictStr | None = None
    EmailAddressMetadataList: list[ConnectEmailAddressSummary] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
