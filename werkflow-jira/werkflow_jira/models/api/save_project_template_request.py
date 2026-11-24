from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .custom_template_options import CustomTemplateOptions


class SaveProjectTemplateRequest(BaseModel):
    projectId: StrictInt | None = None
    templateGenerationOptions: CustomTemplateOptions | None = None
    templateType: StrictStr | None = None
