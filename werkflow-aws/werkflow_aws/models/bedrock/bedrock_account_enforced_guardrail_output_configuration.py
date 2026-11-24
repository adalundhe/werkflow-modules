from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_model_enforcement import BedrockModelEnforcement
from .bedrock_selective_content_guarding import BedrockSelectiveContentGuarding


class BedrockAccountEnforcedGuardrailOutputConfiguration(BaseModel):
    configId: StrictStr | None = None
    guardrailArn: StrictStr | None = None
    guardrailId: StrictStr | None = None
    inputTags: StrictStr | None = None
    selectiveContentGuarding: BedrockSelectiveContentGuarding | None = None
    guardrailVersion: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    owner: StrictStr | None = None
    modelEnforcement: BedrockModelEnforcement | None = None
