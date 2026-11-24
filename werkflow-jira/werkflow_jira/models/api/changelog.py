from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .change_details import ChangeDetails
from .history_metadata import HistoryMetadata
from .user_details import UserDetails


class Changelog(BaseModel):
    author: UserDetails | None = None
    created: StrictStr | None = None
    historyMetadata: HistoryMetadata | None = None
    id: StrictStr | None = None
    items: list[ChangeDetails] | None = None
