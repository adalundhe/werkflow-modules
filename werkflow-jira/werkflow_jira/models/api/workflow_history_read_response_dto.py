from __future__ import annotations
from pydantic import BaseModel
from .workflow_document_dto import WorkflowDocumentDTO
from .workflow_document_status_dto import WorkflowDocumentStatusDTO


class WorkflowHistoryReadResponseDTO(BaseModel):
    statuses: list[WorkflowDocumentStatusDTO] | None = None
    workflows: list[WorkflowDocumentDTO] | None = None
