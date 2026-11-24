from __future__ import annotations
from pydantic import BaseModel
from .project_feature import ProjectFeature


class ContainerForProjectFeatures(BaseModel):
    features: list[ProjectFeature] | None = None
