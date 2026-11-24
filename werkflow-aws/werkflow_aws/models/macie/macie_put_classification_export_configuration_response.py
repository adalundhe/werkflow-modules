from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_classification_export_configuration import MacieClassificationExportConfiguration


class MaciePutClassificationExportConfigurationResponse(BaseModel):
    configuration: MacieClassificationExportConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
