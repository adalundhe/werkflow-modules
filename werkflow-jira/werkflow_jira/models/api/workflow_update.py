from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .document_version import DocumentVersion
from .status_layout_update import StatusLayoutUpdate
from .status_mapping_dto import StatusMappingDTO
from .status_migration import StatusMigration
from .transition_update_dto import TransitionUpdateDTO
from .workflow_layout import WorkflowLayout


class WorkflowUpdate(BaseModel):
    model_config = ConfigDict(extra="allow")

    defaultStatusMappings: list[StatusMigration] | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    loopedTransitionContainerLayout: WorkflowLayout | None = None
    startPointLayout: WorkflowLayout | None = None
    statusMappings: list[StatusMappingDTO] | None = None
    statuses: list[StatusLayoutUpdate] | None = None
    transitions: list[TransitionUpdateDTO] | None = None
    version: DocumentVersion | None = None
