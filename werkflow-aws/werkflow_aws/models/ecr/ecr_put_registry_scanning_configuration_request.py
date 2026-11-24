from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ecr_registry_scanning_rule import ECRRegistryScanningRule


class ECRPutRegistryScanningConfigurationRequest(BaseModel):
    scanType: Literal['BASIC', 'ENHANCED'] | None = None
    rules: list[ECRRegistryScanningRule] | None = None
