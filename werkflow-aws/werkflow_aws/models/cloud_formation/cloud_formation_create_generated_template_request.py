from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_resource_definition import CloudFormationResourceDefinition
from .cloud_formation_template_configuration import CloudFormationTemplateConfiguration


class CloudFormationCreateGeneratedTemplateRequest(BaseModel):
    GeneratedTemplateName: StrictStr
    Resources: list[CloudFormationResourceDefinition] | None = None
    StackName: StrictStr | None = None
    TemplateConfiguration: CloudFormationTemplateConfiguration | None = None
