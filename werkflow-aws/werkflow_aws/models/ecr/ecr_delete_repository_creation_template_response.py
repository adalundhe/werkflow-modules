from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_repository_creation_template import ECRRepositoryCreationTemplate


class ECRDeleteRepositoryCreationTemplateResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryCreationTemplate: ECRRepositoryCreationTemplate | None = None
    ResponseMetadata: dict[str, Any] | None = None
