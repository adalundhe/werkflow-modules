from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_attachment_state_change import ECSAttachmentStateChange
from .ecs_container_state_change import ECSContainerStateChange
from .ecs_managed_agent_state_change import ECSManagedAgentStateChange


class ECSSubmitTaskStateChangeRequest(BaseModel):
    cluster: StrictStr | None = None
    task: StrictStr | None = None
    status: StrictStr | None = None
    reason: StrictStr | None = None
    containers: list[ECSContainerStateChange] | None = None
    attachments: list[ECSAttachmentStateChange] | None = None
    managedAgents: list[ECSManagedAgentStateChange] | None = None
    pullStartedAt: datetime.datetime | StrictStr | None = None
    pullStoppedAt: datetime.datetime | StrictStr | None = None
    executionStoppedAt: datetime.datetime | StrictStr | None = None
