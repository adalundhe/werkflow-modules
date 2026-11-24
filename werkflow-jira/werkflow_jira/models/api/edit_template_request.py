from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .custom_template_options import CustomTemplateOptions


class EditTemplateRequest(BaseModel):
    templateDescription: StrictStr | None = None
    templateGenerationOptions: CustomTemplateOptions | None = None
    templateKey: StrictStr | None = None
    templateName: StrictStr | None = None
