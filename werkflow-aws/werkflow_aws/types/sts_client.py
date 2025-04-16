from abc import ABC, abstractmethod
from typing import Any, Literal

PolicyArn = dict[
    Literal["arn"],
    str,
]

Tag = dict[
    Literal['Key', 'Value'],
    str,
]

ProvidedContext = dict[
    Literal["ProviderArn", "ContextAssertion"],
    str,
]


    # RoleArn='string',
    # RoleSessionName='string',
    # PolicyArns=[
    #     {
    #         'arn': 'string'
    #     },
    # ],
    # Policy='string',
    # DurationSeconds=123,
    # Tags=[
    #     {
    #         'Key': 'string',
    #         'Value': 'string'
    #     },
    # ],
    # TransitiveTagKeys=[
    #     'string',
    # ],
    # ExternalId='string',
    # SerialNumber='string',
    # TokenCode='string',
    # SourceIdentity='string',
    # ProvidedContexts=[
    #     {
    #         'ProviderArn': 'string',
    #         'ContextAssertion': 'string'
    #     },
    # ]

class STSClient(ABC):

    @abstractmethod
    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: list[PolicyArn] | None = None,
        Policy: str | None = None,
        DurationSeconds: int | None = None,
        Tags: list[Tag] | None = None,
        TransitiveTagKeys: list[str] | None = None,
        ExternalId: str | None = None,
        SerialNumber: str | None = None,
        TokenCode: str | None = None,
        SourceIdentity: str | None = None,
        ProvidedContexts: list[ProvidedContext] | None = None,
    ) -> dict[str, Any]:
        pass