from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_resource_definition import CloudFormationResourceDefinition
from .cloud_formation_template_configuration import CloudFormationTemplateConfiguration


class CloudFormationUpdateGeneratedTemplateRequest(BaseModel):
    GeneratedTemplateName: StrictStr
    NewGeneratedTemplateName: StrictStr | None = None
    AddResources: list[CloudFormationResourceDefinition] | None = None
    RemoveResources: list[StrictStr] | None = None
    RefreshAllResources: StrictBool | None = None
    TemplateConfiguration: CloudFormationTemplateConfiguration | None = None
