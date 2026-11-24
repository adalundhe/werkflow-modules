from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .notification_scheme_and_project_mapping_json_bean import NotificationSchemeAndProjectMappingJsonBean


class PageBeanNotificationSchemeAndProjectMappingJsonBean(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[NotificationSchemeAndProjectMappingJsonBean] | None = None
