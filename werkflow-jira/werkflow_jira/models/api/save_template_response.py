from __future__ import annotations
from pydantic import BaseModel
from .project_template_key import ProjectTemplateKey


class SaveTemplateResponse(BaseModel):
    projectTemplateKey: ProjectTemplateKey | None = None
