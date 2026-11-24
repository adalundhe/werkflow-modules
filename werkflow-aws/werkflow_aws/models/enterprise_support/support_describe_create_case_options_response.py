from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .support_communication_type_options import SupportCommunicationTypeOptions


class SupportDescribeCreateCaseOptionsResponse(BaseModel):
    languageAvailability: StrictStr | None = None
    communicationTypes: list[SupportCommunicationTypeOptions] | None = None
    ResponseMetadata: dict[str, Any] | None = None
