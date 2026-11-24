from __future__ import annotations
from pydantic import BaseModel
from .connect_task_template_field_identifier import ConnectTaskTemplateFieldIdentifier


class ConnectInvisibleFieldInfo(BaseModel):
    Id: ConnectTaskTemplateFieldIdentifier | None = None
