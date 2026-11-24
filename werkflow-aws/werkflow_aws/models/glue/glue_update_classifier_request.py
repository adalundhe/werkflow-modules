from __future__ import annotations
from pydantic import BaseModel
from .glue_update_csv_classifier_request import GlueUpdateCsvClassifierRequest
from .glue_update_grok_classifier_request import GlueUpdateGrokClassifierRequest
from .glue_update_json_classifier_request import GlueUpdateJsonClassifierRequest
from .glue_update_xml_classifier_request import GlueUpdateXMLClassifierRequest


class GlueUpdateClassifierRequest(BaseModel):
    GrokClassifier: GlueUpdateGrokClassifierRequest | None = None
    XMLClassifier: GlueUpdateXMLClassifierRequest | None = None
    JsonClassifier: GlueUpdateJsonClassifierRequest | None = None
    CsvClassifier: GlueUpdateCsvClassifierRequest | None = None
