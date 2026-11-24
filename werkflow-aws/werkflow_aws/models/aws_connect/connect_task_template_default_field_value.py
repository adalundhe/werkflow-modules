from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_task_template_field_identifier import ConnectTaskTemplateFieldIdentifier


class ConnectTaskTemplateDefaultFieldValue(BaseModel):
    Id: ConnectTaskTemplateFieldIdentifier | None = None
    DefaultValue: StrictStr | None = None
