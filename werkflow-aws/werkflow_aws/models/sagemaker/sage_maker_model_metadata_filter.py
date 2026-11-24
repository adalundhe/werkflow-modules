from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerModelMetadataFilter(BaseModel):
    Name: Literal['Domain', 'Framework', 'Task', 'FrameworkVersion']
    Value: StrictStr
