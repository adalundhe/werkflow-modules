from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_parameter import CloudFormationParameter


class CloudFormationEstimateTemplateCostRequest(BaseModel):
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    Parameters: list[CloudFormationParameter] | None = None
