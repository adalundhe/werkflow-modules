from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .transition_payload import TransitionPayload
from .workflow_status_layout_payload import WorkflowStatusLayoutPayload
from .workflow_status_payload import WorkflowStatusPayload


class WorkflowPayload(BaseModel):
    description: StrictStr | None = None
    loopedTransitionContainerLayout: WorkflowStatusLayoutPayload | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    startPointLayout: WorkflowStatusLayoutPayload | None = None
    statuses: list[WorkflowStatusPayload] | None = None
    transitions: list[TransitionPayload] | None = None
