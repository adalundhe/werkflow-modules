from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockAutomatedReasoningPolicyBuildWorkflowDocument(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    document: StrictBytes | BinaryIO | StrictStr
    documentContentType: Literal['pdf', 'txt']
    documentName: StrictStr
    documentDescription: StrictStr | None = None
