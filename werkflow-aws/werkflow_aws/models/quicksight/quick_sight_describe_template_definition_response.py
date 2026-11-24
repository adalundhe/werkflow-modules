from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_template_error import QuickSightTemplateError
from .quick_sight_template_version_definition import QuickSightTemplateVersionDefinition


class QuickSightDescribeTemplateDefinitionResponse(BaseModel):
    Name: StrictStr | None = None
    TemplateId: StrictStr | None = None
    Errors: list[QuickSightTemplateError] | None = None
    ResourceStatus: StrictStr | None = None
    ThemeArn: StrictStr | None = None
    Definition: QuickSightTemplateVersionDefinition | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
