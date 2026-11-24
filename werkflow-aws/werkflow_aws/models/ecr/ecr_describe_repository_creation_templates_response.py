from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_repository_creation_template import ECRRepositoryCreationTemplate


class ECRDescribeRepositoryCreationTemplatesResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryCreationTemplates: list[ECRRepositoryCreationTemplate] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
