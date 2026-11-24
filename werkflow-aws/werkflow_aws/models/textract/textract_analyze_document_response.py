from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_block import TextractBlock
from .textract_document_metadata import TextractDocumentMetadata
from .textract_human_loop_activation_output import TextractHumanLoopActivationOutput


class TextractAnalyzeDocumentResponse(BaseModel):
    DocumentMetadata: TextractDocumentMetadata | None = None
    Blocks: list[TextractBlock] | None = None
    HumanLoopActivationOutput: TextractHumanLoopActivationOutput | None = None
    AnalyzeDocumentModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
