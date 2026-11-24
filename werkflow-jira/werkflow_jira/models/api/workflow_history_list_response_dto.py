from __future__ import annotations
from pydantic import BaseModel
from .workflow_history_item_dto import WorkflowHistoryItemDTO


class WorkflowHistoryListResponseDTO(BaseModel):
    entries: list[WorkflowHistoryItemDTO] | None = None
