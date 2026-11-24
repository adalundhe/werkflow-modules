from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_associated_contact_summary import ConnectAssociatedContactSummary


class ConnectListAssociatedContactsResponse(BaseModel):
    ContactSummaryList: list[ConnectAssociatedContactSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
