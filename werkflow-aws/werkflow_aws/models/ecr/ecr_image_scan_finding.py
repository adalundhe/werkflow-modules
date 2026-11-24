from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_attribute import ECRAttribute


class ECRImageScanFinding(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    uri: StrictStr | None = None
    severity: StrictStr | None = None
    attributes: list[ECRAttribute] | None = None
