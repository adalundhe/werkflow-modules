from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_attachment_information import SSMAttachmentInformation
from .ssm_document_parameter import SSMDocumentParameter
from .ssm_document_requires import SSMDocumentRequires
from .ssm_review_information import SSMReviewInformation
from .ssm_tag import SSMTag


class SSMDocumentDescription(BaseModel):
    Sha1: StrictStr | None = None
    Hash: StrictStr | None = None
    HashType: StrictStr | None = None
    Name: StrictStr | None = None
    DisplayName: StrictStr | None = None
    VersionName: StrictStr | None = None
    Owner: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusInformation: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: list[SSMDocumentParameter] | None = None
    PlatformTypes: list[StrictStr] | None = None
    DocumentType: StrictStr | None = None
    SchemaVersion: StrictStr | None = None
    LatestVersion: StrictStr | None = None
    DefaultVersion: StrictStr | None = None
    DocumentFormat: StrictStr | None = None
    TargetType: StrictStr | None = None
    Tags: list[SSMTag] | None = None
    AttachmentsInformation: list[SSMAttachmentInformation] | None = None
    Requires: list[SSMDocumentRequires] | None = None
    Author: StrictStr | None = None
    ReviewInformation: list[SSMReviewInformation] | None = None
    ApprovedVersion: StrictStr | None = None
    PendingReviewVersion: StrictStr | None = None
    ReviewStatus: StrictStr | None = None
    Category: list[StrictStr] | None = None
    CategoryEnum: list[StrictStr] | None = None
    CloudProviders: list[StrictStr] | None = None
