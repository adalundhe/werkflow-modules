from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceTemplateSSMDocumentDetails(BaseModel):
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
