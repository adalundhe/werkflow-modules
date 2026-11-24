from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_template_summary_config import CloudFormationTemplateSummaryConfig


class CloudFormationGetTemplateSummaryRequest(BaseModel):
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    StackName: StrictStr | None = None
    StackSetName: StrictStr | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
    TemplateSummaryConfig: CloudFormationTemplateSummaryConfig | None = None
