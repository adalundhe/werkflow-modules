from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_project_description import RekognitionProjectDescription


class RekognitionDescribeProjectsResponse(BaseModel):
    ProjectDescriptions: list[RekognitionProjectDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
