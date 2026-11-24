from __future__ import annotations
from pydantic import BaseModel
from .custom_template_request_dto import CustomTemplateRequestDTO
from .custom_templates_project_details import CustomTemplatesProjectDetails


class ProjectCustomTemplateCreateRequestDTO(BaseModel):
    details: CustomTemplatesProjectDetails | None = None
    template: CustomTemplateRequestDTO | None = None
