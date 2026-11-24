from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_minimum_throughput_billing_commitment_output import KinesisMinimumThroughputBillingCommitmentOutput


class KinesisDescribeAccountSettingsResponse(BaseModel):
    MinimumThroughputBillingCommitment: KinesisMinimumThroughputBillingCommitmentOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
