from __future__ import annotations
from pydantic import BaseModel
from .lex_bot_import_specification import LexBotImportSpecification
from .lex_bot_locale_import_specification import LexBotLocaleImportSpecification
from .lex_custom_vocabulary_import_specification import LexCustomVocabularyImportSpecification
from .lex_test_set_import_resource_specification import LexTestSetImportResourceSpecification


class LexImportResourceSpecification(BaseModel):
    botImportSpecification: LexBotImportSpecification | None = None
    botLocaleImportSpecification: LexBotLocaleImportSpecification | None = None
    customVocabularyImportSpecification: LexCustomVocabularyImportSpecification | None = None
    testSetImportResourceSpecification: LexTestSetImportResourceSpecification | None = None
