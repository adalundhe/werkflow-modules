from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_annotated_chunk import BedrockAutomatedReasoningPolicyAnnotatedChunk
from .bedrock_automated_reasoning_policy_atomic_statement import BedrockAutomatedReasoningPolicyAtomicStatement


class BedrockAutomatedReasoningPolicyReportSourceDocument(BaseModel):
    documentName: StrictStr | None = None
    documentHash: StrictStr | None = None
    documentId: StrictStr | None = None
    atomicStatements: list[BedrockAutomatedReasoningPolicyAtomicStatement] | None = None
    documentContent: list[BedrockAutomatedReasoningPolicyAnnotatedChunk] | None = None
