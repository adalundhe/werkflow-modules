from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockAutomatedReasoningPolicySourceDocument(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    document: StrictBytes | Any | None = None
    documentContentType: StrictStr | None = None
    documentName: StrictStr | None = None
    documentDescription: StrictStr | None = None
    documentHash: StrictStr | None = None
