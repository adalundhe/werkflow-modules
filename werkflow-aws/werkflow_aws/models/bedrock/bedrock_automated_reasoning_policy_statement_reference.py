from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyStatementReference(BaseModel):
    documentId: StrictStr | None = None
    statementId: StrictStr | None = None
