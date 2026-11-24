from __future__ import annotations
from pydantic import BaseModel
from .connect_task_template_default_field_value import ConnectTaskTemplateDefaultFieldValue


class ConnectTaskTemplateDefaults(BaseModel):
    DefaultFieldValues: list[ConnectTaskTemplateDefaultFieldValue] | None = None
