from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_task_template_constraints import ConnectTaskTemplateConstraints
from .connect_task_template_contact_hooks import ConnectTaskTemplateContactHooks
from .connect_task_template_defaults import ConnectTaskTemplateDefaults
from .connect_task_template_field import ConnectTaskTemplateField


class ConnectUpdateTaskTemplateResponse(BaseModel):
    InstanceId: StrictStr | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ContactFlowId: StrictStr | None = None
    SelfAssignFlowId: StrictStr | None = None
    ContactHooks: ConnectTaskTemplateContactHooks | None = None
    Constraints: ConnectTaskTemplateConstraints | None = None
    Defaults: ConnectTaskTemplateDefaults | None = None
    Fields: list[ConnectTaskTemplateField] | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
