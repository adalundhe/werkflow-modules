from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_template_summary import CloudFormationTemplateSummary


class CloudFormationListGeneratedTemplatesResponse(BaseModel):
    Summaries: list[CloudFormationTemplateSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
