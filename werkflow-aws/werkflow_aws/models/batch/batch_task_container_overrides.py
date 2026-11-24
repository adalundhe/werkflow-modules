from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_key_value_pair import BatchKeyValuePair
from .batch_resource_requirement import BatchResourceRequirement


class BatchTaskContainerOverrides(BaseModel):
    command: list[StrictStr] | None = None
    environment: list[BatchKeyValuePair] | None = None
    name: StrictStr | None = None
    resourceRequirements: list[BatchResourceRequirement] | None = None
