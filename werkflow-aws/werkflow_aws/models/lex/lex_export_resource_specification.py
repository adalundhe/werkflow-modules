from __future__ import annotations
from pydantic import BaseModel
from .lex_bot_export_specification import LexBotExportSpecification
from .lex_bot_locale_export_specification import LexBotLocaleExportSpecification
from .lex_custom_vocabulary_export_specification import LexCustomVocabularyExportSpecification
from .lex_test_set_export_specification import LexTestSetExportSpecification


class LexExportResourceSpecification(BaseModel):
    botExportSpecification: LexBotExportSpecification | None = None
    botLocaleExportSpecification: LexBotLocaleExportSpecification | None = None
    customVocabularyExportSpecification: LexCustomVocabularyExportSpecification | None = None
    testSetExportSpecification: LexTestSetExportSpecification | None = None
