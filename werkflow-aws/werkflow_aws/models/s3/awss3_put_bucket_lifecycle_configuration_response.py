from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel


class AWSS3PutBucketLifecycleConfigurationResponse(BaseModel):
    TransitionDefaultMinimumObjectSize: Literal['varies_by_storage_class', 'all_storage_classes_128K'] | None = None
    ResponseMetadata: dict[str, Any] | None = None
