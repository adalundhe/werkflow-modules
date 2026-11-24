from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel
from .awss3_lifecycle_rule import AWSS3LifecycleRule


class AWSS3GetBucketLifecycleConfigurationResponse(BaseModel):
    Rules: list[AWSS3LifecycleRule] | None = None
    TransitionDefaultMinimumObjectSize: Literal['varies_by_storage_class', 'all_storage_classes_128K'] | None = None
    ResponseMetadata: dict[str, Any] | None = None
