from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_project_version_description import RekognitionProjectVersionDescription


class RekognitionDescribeProjectVersionsResponse(BaseModel):
    ProjectVersionDescriptions: list[RekognitionProjectVersionDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
