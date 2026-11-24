from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lex_test_execution_target import LexTestExecutionTarget


class LexStartTestExecutionRequest(BaseModel):
    testSetId: StrictStr
    target: LexTestExecutionTarget
    apiMode: Literal['Streaming', 'NonStreaming']
    testExecutionModality: Literal['Text', 'Audio'] | None = None
