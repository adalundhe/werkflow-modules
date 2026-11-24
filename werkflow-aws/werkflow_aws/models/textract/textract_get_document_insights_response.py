from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_output_configuration import TextractOutputConfiguration


class TextractGetDocumentInsightsResponse(BaseModel):
    Status: StrictStr | None = None
    OutputConfiguration: TextractOutputConfiguration | None = None
    ErrorType: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
