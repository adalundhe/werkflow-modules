from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .cloud_watch_logs_log_fields_list_item import CloudWatchLogsLogFieldsListItem


class CloudWatchLogsLogFieldType(BaseModel):
    type: StrictStr | None = None
    element: CloudWatchLogsLogFieldType | None = None
    fields: list[CloudWatchLogsLogFieldsListItem] | None = None
