from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_registry_scanning_rule import ECRRegistryScanningRule


class ECRRegistryScanningConfiguration(BaseModel):
    scanType: StrictStr | None = None
    rules: list[ECRRegistryScanningRule] | None = None
