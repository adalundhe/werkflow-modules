from __future__ import annotations
from pydantic import BaseModel
from .lex_overall_test_result_item import LexOverallTestResultItem


class LexOverallTestResults(BaseModel):
    items: list[LexOverallTestResultItem] | None = None
