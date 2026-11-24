from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_layout_update import StatusLayoutUpdate
from .transition_update_dto import TransitionUpdateDTO
from .workflow_layout import WorkflowLayout


class WorkflowCreate(BaseModel):
    description: StrictStr | None = None
    loopedTransitionContainerLayout: WorkflowLayout | None = None
    name: StrictStr | None = None
    startPointLayout: WorkflowLayout | None = None
    statuses: list[StatusLayoutUpdate] | None = None
    transitions: list[TransitionUpdateDTO] | None = None
