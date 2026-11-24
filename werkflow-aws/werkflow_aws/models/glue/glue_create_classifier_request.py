from __future__ import annotations
from pydantic import BaseModel
from .glue_create_csv_classifier_request import GlueCreateCsvClassifierRequest
from .glue_create_grok_classifier_request import GlueCreateGrokClassifierRequest
from .glue_create_json_classifier_request import GlueCreateJsonClassifierRequest
from .glue_create_xml_classifier_request import GlueCreateXMLClassifierRequest


class GlueCreateClassifierRequest(BaseModel):
    GrokClassifier: GlueCreateGrokClassifierRequest | None = None
    XMLClassifier: GlueCreateXMLClassifierRequest | None = None
    JsonClassifier: GlueCreateJsonClassifierRequest | None = None
    CsvClassifier: GlueCreateCsvClassifierRequest | None = None
