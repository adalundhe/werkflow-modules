from __future__ import annotations
from pydantic import BaseModel
from .glue_csv_classifier import GlueCsvClassifier
from .glue_grok_classifier import GlueGrokClassifier
from .glue_json_classifier import GlueJsonClassifier
from .glue_xml_classifier import GlueXMLClassifier


class GlueClassifier(BaseModel):
    GrokClassifier: GlueGrokClassifier | None = None
    XMLClassifier: GlueXMLClassifier | None = None
    JsonClassifier: GlueJsonClassifier | None = None
    CsvClassifier: GlueCsvClassifier | None = None
