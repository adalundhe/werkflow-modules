from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_task_template_constraints import ConnectTaskTemplateConstraints
from .connect_task_template_contact_hooks import ConnectTaskTemplateContactHooks
from .connect_task_template_defaults import ConnectTaskTemplateDefaults
from .connect_task_template_field import ConnectTaskTemplateField


class ConnectCreateTaskTemplateRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Fields: list[ConnectTaskTemplateField]
    Description: StrictStr | None = None
    ContactFlowId: StrictStr | None = None
    SelfAssignFlowId: StrictStr | None = None
    ContactHooks: ConnectTaskTemplateContactHooks | None = None
    Constraints: ConnectTaskTemplateConstraints | None = None
    Defaults: ConnectTaskTemplateDefaults | None = None
    Status: Literal['ACTIVE', 'INACTIVE'] | None = None
    ClientToken: StrictStr | None = None
