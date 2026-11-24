from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_task_template_field_identifier import ConnectTaskTemplateFieldIdentifier


class ConnectTaskTemplateField(BaseModel):
    Id: ConnectTaskTemplateFieldIdentifier | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    SingleSelectOptions: list[StrictStr] | None = None
