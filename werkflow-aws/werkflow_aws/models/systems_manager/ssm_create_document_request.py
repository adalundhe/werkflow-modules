from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ssm_attachments_source import SSMAttachmentsSource
from .ssm_document_requires import SSMDocumentRequires
from .ssm_tag import SSMTag


class SSMCreateDocumentRequest(BaseModel):
    Content: StrictStr
    Name: StrictStr
    Requires: list[SSMDocumentRequires] | None = None
    Attachments: list[SSMAttachmentsSource] | None = None
    DisplayName: StrictStr | None = None
    VersionName: StrictStr | None = None
    DocumentType: Literal['Command', 'Policy', 'Automation', 'Session', 'Package', 'ApplicationConfiguration', 'ApplicationConfigurationSchema', 'DeploymentStrategy', 'ChangeCalendar', 'Automation.ChangeTemplate', 'ProblemAnalysis', 'ProblemAnalysisTemplate', 'CloudFormation', 'ConformancePackTemplate', 'QuickSetup', 'ManualApprovalPolicy', 'AutoApprovalPolicy'] | None = None
    DocumentFormat: Literal['YAML', 'JSON', 'TEXT'] | None = None
    TargetType: StrictStr | None = None
    Tags: list[SSMTag] | None = None
    CloudProviders: list[Literal['AWS', 'Azure', 'GCP']] | None = None
