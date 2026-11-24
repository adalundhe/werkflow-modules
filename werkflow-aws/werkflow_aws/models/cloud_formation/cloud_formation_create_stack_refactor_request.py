from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_resource_mapping import CloudFormationResourceMapping
from .cloud_formation_stack_definition import CloudFormationStackDefinition


class CloudFormationCreateStackRefactorRequest(BaseModel):
    StackDefinitions: list[CloudFormationStackDefinition]
    Description: StrictStr | None = None
    EnableStackCreation: StrictBool | None = None
    ResourceMappings: list[CloudFormationResourceMapping] | None = None
