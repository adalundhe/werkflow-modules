from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_configuration_revision_model import MSKConfigurationRevisionModel


class MSKListConfigurationRevisionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Revisions: list[MSKConfigurationRevisionModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
