from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .notification_scheme_event_payload import NotificationSchemeEventPayload
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class NotificationSchemePayload(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    notificationSchemeEvents: list[NotificationSchemeEventPayload] | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
