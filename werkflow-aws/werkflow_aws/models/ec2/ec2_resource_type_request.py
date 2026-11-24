from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ec2_resource_type_option import EC2ResourceTypeOption


class EC2ResourceTypeRequest(BaseModel):
    ResourceType: Literal['ec2:Instance', 'ec2:LaunchTemplate', 'ssm:Parameter', 'imagebuilder:ImageRecipe', 'imagebuilder:ContainerRecipe'] | None = None
    ResourceTypeOptions: list[EC2ResourceTypeOption] | None = None
