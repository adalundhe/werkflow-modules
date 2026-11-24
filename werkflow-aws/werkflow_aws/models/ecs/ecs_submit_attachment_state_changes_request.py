from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_attachment_state_change import ECSAttachmentStateChange


class ECSSubmitAttachmentStateChangesRequest(BaseModel):
    attachments: list[ECSAttachmentStateChange]
    cluster: StrictStr | None = None
