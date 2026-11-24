from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_version import DocumentVersion


class WorkflowMetadataRestModel(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    version: DocumentVersion | None = None
