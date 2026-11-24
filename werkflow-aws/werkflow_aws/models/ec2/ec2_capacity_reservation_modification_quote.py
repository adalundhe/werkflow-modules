from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_modification_quote_current_configuration import EC2ModificationQuoteCurrentConfiguration
from .ec2_modification_terms import EC2ModificationTerms
from .ec2_tag_model import EC2TagModel


class EC2CapacityReservationModificationQuote(BaseModel):
    CapacityReservationModificationQuoteId: StrictStr | None = None
    CapacityReservationId: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    QuoteState: StrictStr | None = None
    CurrentConfiguration: EC2ModificationQuoteCurrentConfiguration | None = None
    ModificationTerms: EC2ModificationTerms | None = None
    Tags: list[EC2TagModel] | None = None
