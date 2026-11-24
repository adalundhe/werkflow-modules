from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_key_value_pair import BatchKeyValuePair
from .batch_resource_requirement import BatchResourceRequirement


class BatchContainerOverrides(BaseModel):
    vcpus: StrictInt | None = None
    memory: StrictInt | None = None
    command: list[StrictStr] | None = None
    instanceType: StrictStr | None = None
    environment: list[BatchKeyValuePair] | None = None
    resourceRequirements: list[BatchResourceRequirement] | None = None
