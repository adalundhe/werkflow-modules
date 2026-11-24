from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .textract_adapters_config import TextractAdaptersConfig
from .textract_document import TextractDocument
from .textract_human_loop_config import TextractHumanLoopConfig
from .textract_queries_config import TextractQueriesConfig


class TextractAnalyzeDocumentRequest(BaseModel):
    Document: TextractDocument
    FeatureTypes: list[Literal['TABLES', 'FORMS', 'QUERIES', 'SIGNATURES', 'LAYOUT']]
    HumanLoopConfig: TextractHumanLoopConfig | None = None
    QueriesConfig: TextractQueriesConfig | None = None
    AdaptersConfig: TextractAdaptersConfig | None = None
