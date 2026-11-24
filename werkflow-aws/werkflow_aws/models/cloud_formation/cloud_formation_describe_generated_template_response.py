from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_formation_resource_detail import CloudFormationResourceDetail
from .cloud_formation_template_configuration import CloudFormationTemplateConfiguration
from .cloud_formation_template_progress import CloudFormationTemplateProgress


class CloudFormationDescribeGeneratedTemplateResponse(BaseModel):
    GeneratedTemplateId: StrictStr | None = None
    GeneratedTemplateName: StrictStr | None = None
    Resources: list[CloudFormationResourceDetail] | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Progress: CloudFormationTemplateProgress | None = None
    StackId: StrictStr | None = None
    TemplateConfiguration: CloudFormationTemplateConfiguration | None = None
    TotalWarnings: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
