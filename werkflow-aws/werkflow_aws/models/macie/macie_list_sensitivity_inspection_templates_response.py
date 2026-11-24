from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_sensitivity_inspection_templates_entry import MacieSensitivityInspectionTemplatesEntry


class MacieListSensitivityInspectionTemplatesResponse(BaseModel):
    nextToken: StrictStr | None = None
    sensitivityInspectionTemplates: list[MacieSensitivityInspectionTemplatesEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
