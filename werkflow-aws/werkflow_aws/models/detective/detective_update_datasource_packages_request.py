from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DetectiveUpdateDatasourcePackagesRequest(BaseModel):
    GraphArn: StrictStr
    DatasourcePackages: list[Literal['DETECTIVE_CORE', 'EKS_AUDIT', 'ASFF_SECURITYHUB_FINDING']]
