from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchAnalysisOptions(BaseModel):
    Synonyms: StrictStr | None = None
    Stopwords: StrictStr | None = None
    StemmingDictionary: StrictStr | None = None
    JapaneseTokenizationDictionary: StrictStr | None = None
    AlgorithmicStemming: StrictStr | None = None
