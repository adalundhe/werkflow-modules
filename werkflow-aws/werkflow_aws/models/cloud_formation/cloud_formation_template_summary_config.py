from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudFormationTemplateSummaryConfig(BaseModel):
    TreatUnrecognizedResourceTypesAsWarnings: StrictBool | None = None
