from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_document_parameter import IoTDocumentParameter


class IoTDescribeManagedJobTemplateResponse(BaseModel):
    templateName: StrictStr | None = None
    templateArn: StrictStr | None = None
    description: StrictStr | None = None
    templateVersion: StrictStr | None = None
    environments: list[StrictStr] | None = None
    documentParameters: list[IoTDocumentParameter] | None = None
    document: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
