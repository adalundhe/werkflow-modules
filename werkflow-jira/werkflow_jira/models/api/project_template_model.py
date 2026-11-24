from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .custom_template_options import CustomTemplateOptions
from .project_archetype import ProjectArchetype
from .project_template_key import ProjectTemplateKey


class ProjectTemplateModel(BaseModel):
    archetype: ProjectArchetype | None = None
    defaultBoardView: StrictStr | None = None
    description: StrictStr | None = None
    liveTemplateProjectIdReference: StrictInt | None = None
    name: StrictStr | None = None
    projectTemplateKey: ProjectTemplateKey | None = None
    snapshotTemplate: dict[StrictStr, Any] | None = None
    templateGenerationOptions: CustomTemplateOptions | None = None
    type: StrictStr | None = None
