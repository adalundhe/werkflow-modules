from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_cancellation_terms import EC2CancellationTerms
from .ec2_capacity_reservation_configuration import EC2CapacityReservationConfiguration
from .ec2_tag_model import EC2TagModel


class EC2CapacityReservationCancellationQuote(BaseModel):
    CapacityReservationCancellationQuoteId: StrictStr | None = None
    CapacityReservationId: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    QuoteState: StrictStr | None = None
    CurrentConfiguration: EC2CapacityReservationConfiguration | None = None
    CancellationTerms: list[EC2CancellationTerms] | None = None
    Tags: list[EC2TagModel] | None = None
