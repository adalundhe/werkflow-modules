from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_template_parameter import CloudFormationTemplateParameter


class CloudFormationValidateTemplateResponse(BaseModel):
    Parameters: list[CloudFormationTemplateParameter] | None = None
    Description: StrictStr | None = None
    Capabilities: list[StrictStr] | None = None
    CapabilitiesReason: StrictStr | None = None
    DeclaredTransforms: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
