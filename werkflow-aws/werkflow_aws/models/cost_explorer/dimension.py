from pydantic import BaseModel, StrictStr, Field, conlist
from typing import Literal
from .match_option_types import MatchOptionTypes


DimensionKeys = Literal[
    "AZ",
    "INSTANCE_TYPE",
    "LINKED_ACCOUNT",
    "LINKED_ACCOUNT_NAME",
    "OPERATION",
    "PURCHASE_TYPE",
    "REGION",
    "SERVICE",
    "SERVICE_CODE",
    "USAGE_TYPE",
    "USAGE_TYPE_GROUP",
    "RECORD_TYPE",
    "OPERATING_SYSTEM",
    "TENANCY",
    "SCOPE",
    "PLATFORM",
    "SUBSCRIPTION_ID",
    "LEGAL_ENTITY_NAME",
    "DEPLOYMENT_OPTION",
    "DATABASE_ENGINE",
    "CACHE_ENGINE",
    "INSTANCE_TYPE_FAMILY",
    "BILLING_ENTITY",
    "RESERVATION_ID",
    "RESOURCE_ID",
    "RIGHTSIZING_TYPE",
    "SAVINGS_PLANS_TYPE",
    "SAVINGS_PLAN_ARN",
    "PAYMENT_OPTION",
    "AGREEMENT_END_DATE_TIME_AFTER",
    "AGREEMENT_END_DATE_TIME_BEFORE",
    "INVOICING_ENTITY",
    "ANOMALY_TOTAL_IMPACT_ABSOLUTE",
    "ANOMALY_TOTAL_IMPACT_PERCENTAGE",
]


class Dimension(BaseModel):
    Key: DimensionKeys
    MatchOptions: list[MatchOptionTypes]
    Values: list[StrictStr]

    def dump(self):
        return self.model_dump()