from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .save_project_template_request import SaveProjectTemplateRequest


class SaveTemplateRequest(BaseModel):
    templateDescription: StrictStr | None = None
    templateFromProjectRequest: SaveProjectTemplateRequest | None = None
    templateName: StrictStr | None = None
