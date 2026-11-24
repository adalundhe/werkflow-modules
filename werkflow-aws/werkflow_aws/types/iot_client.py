from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class IoTClient(ABC):

    @abstractmethod
    def accept_certificate_transfer(
        self,
        *,
        certificateId: str,
        setAsActive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_thing_to_billing_group(
        self,
        *,
        billingGroupName: str | None = None,
        billingGroupArn: str | None = None,
        thingName: str | None = None,
        thingArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_thing_to_thing_group(
        self,
        *,
        thingGroupName: str | None = None,
        thingGroupArn: str | None = None,
        thingName: str | None = None,
        thingArn: str | None = None,
        overrideDynamicGroups: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_sbom_with_package_version(
        self,
        *,
        packageName: str,
        versionName: str,
        sbom: dict[str, Any],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_targets_with_job(
        self,
        *,
        targets: list[str],
        jobId: str,
        comment: str | None = None,
        namespaceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_policy(
        self,
        *,
        policyName: str,
        target: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_principal_policy(
        self,
        *,
        policyName: str,
        principal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_security_profile(
        self,
        *,
        securityProfileName: str,
        securityProfileTargetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_thing_principal(
        self,
        *,
        thingName: str,
        principal: str,
        thingPrincipalType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_audit_mitigation_actions_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_audit_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_certificate_transfer(
        self,
        *,
        certificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_detect_mitigation_actions_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_job(
        self,
        *,
        jobId: str,
        reasonCode: str | None = None,
        comment: str | None = None,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        force: bool | None = None,
        expectedVersion: int | None = None,
        statusDetails: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def clear_default_authorizer(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_topic_rule_destination(
        self,
        *,
        confirmationToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_audit_suppression(
        self,
        *,
        checkName: str,
        resourceIdentifier: dict[str, Any],
        clientRequestToken: str,
        expirationDate: datetime.datetime | str | None = None,
        suppressIndefinitely: bool | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_authorizer(
        self,
        *,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str | None = None,
        tokenSigningPublicKeys: dict[str, str] | None = None,
        status: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        signingDisabled: bool | None = None,
        enableCachingForHttp: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_billing_group(
        self,
        *,
        billingGroupName: str,
        billingGroupProperties: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_certificate_from_csr(
        self,
        *,
        certificateSigningRequest: str,
        setAsActive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_certificate_provider(
        self,
        *,
        certificateProviderName: str,
        lambdaFunctionArn: str,
        accountDefaultForOperations: list[str],
        clientToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_command(
        self,
        *,
        commandId: str,
        namespace: str | None = None,
        displayName: str | None = None,
        description: str | None = None,
        payload: dict[str, Any] | None = None,
        payloadTemplate: str | None = None,
        preprocessor: dict[str, Any] | None = None,
        mandatoryParameters: list[dict[str, Any]] | None = None,
        roleArn: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_metric(
        self,
        *,
        metricName: str,
        metricType: str,
        clientRequestToken: str,
        displayName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dimension(
        self,
        *,
        name: str,
        type: str,
        stringValues: list[str],
        clientRequestToken: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_configuration(
        self,
        *,
        domainConfigurationName: str,
        domainName: str | None = None,
        serverCertificateArns: list[str] | None = None,
        validationCertificateArn: str | None = None,
        authorizerConfig: dict[str, Any] | None = None,
        serviceType: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        tlsConfig: dict[str, Any] | None = None,
        serverCertificateConfig: dict[str, Any] | None = None,
        authenticationType: str | None = None,
        applicationProtocol: str | None = None,
        clientCertificateConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dynamic_thing_group(
        self,
        *,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: dict[str, Any] | None = None,
        indexName: str | None = None,
        queryVersion: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fleet_metric(
        self,
        *,
        metricName: str,
        queryString: str,
        aggregationType: dict[str, Any],
        period: int,
        aggregationField: str,
        description: str | None = None,
        queryVersion: str | None = None,
        indexName: str | None = None,
        unit: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_job(
        self,
        *,
        jobId: str,
        targets: list[str],
        documentSource: str | None = None,
        document: str | None = None,
        description: str | None = None,
        presignedUrlConfig: dict[str, Any] | None = None,
        targetSelection: str | None = None,
        jobExecutionsRolloutConfig: dict[str, Any] | None = None,
        abortConfig: dict[str, Any] | None = None,
        timeoutConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        namespaceId: str | None = None,
        jobTemplateArn: str | None = None,
        jobExecutionsRetryConfig: dict[str, Any] | None = None,
        documentParameters: dict[str, str] | None = None,
        schedulingConfig: dict[str, Any] | None = None,
        destinationPackageVersions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_job_template(
        self,
        *,
        jobTemplateId: str,
        description: str,
        jobArn: str | None = None,
        documentSource: str | None = None,
        document: str | None = None,
        presignedUrlConfig: dict[str, Any] | None = None,
        jobExecutionsRolloutConfig: dict[str, Any] | None = None,
        abortConfig: dict[str, Any] | None = None,
        timeoutConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        jobExecutionsRetryConfig: dict[str, Any] | None = None,
        maintenanceWindows: list[dict[str, Any]] | None = None,
        destinationPackageVersions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_keys_and_certificate(
        self,
        *,
        setAsActive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_mitigation_action(
        self,
        *,
        actionName: str,
        roleArn: str,
        actionParams: dict[str, Any],
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ota_update(
        self,
        *,
        otaUpdateId: str,
        targets: list[str],
        files: list[dict[str, Any]],
        roleArn: str,
        description: str | None = None,
        protocols: list[str] | None = None,
        targetSelection: str | None = None,
        awsJobExecutionsRolloutConfig: dict[str, Any] | None = None,
        awsJobPresignedUrlConfig: dict[str, Any] | None = None,
        awsJobAbortConfig: dict[str, Any] | None = None,
        awsJobTimeoutConfig: dict[str, Any] | None = None,
        additionalParameters: dict[str, str] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_package(
        self,
        *,
        packageName: str,
        description: str | None = None,
        tags: dict[str, str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_package_version(
        self,
        *,
        packageName: str,
        versionName: str,
        description: str | None = None,
        attributes: dict[str, str] | None = None,
        artifact: dict[str, Any] | None = None,
        recipe: str | None = None,
        tags: dict[str, str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy(
        self,
        *,
        policyName: str,
        policyDocument: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy_version(
        self,
        *,
        policyName: str,
        policyDocument: str,
        setAsDefault: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_provisioning_claim(
        self,
        *,
        templateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_provisioning_template(
        self,
        *,
        templateName: str,
        templateBody: str,
        provisioningRoleArn: str,
        description: str | None = None,
        enabled: bool | None = None,
        preProvisioningHook: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_provisioning_template_version(
        self,
        *,
        templateName: str,
        templateBody: str,
        setAsDefault: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_role_alias(
        self,
        *,
        roleAlias: str,
        roleArn: str,
        credentialDurationSeconds: int | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_scheduled_audit(
        self,
        *,
        frequency: str,
        targetCheckNames: list[str],
        scheduledAuditName: str,
        dayOfMonth: str | None = None,
        dayOfWeek: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_profile(
        self,
        *,
        securityProfileName: str,
        securityProfileDescription: str | None = None,
        behaviors: list[dict[str, Any]] | None = None,
        alertTargets: dict[str, dict[str, Any]] | None = None,
        additionalMetricsToRetain: list[str] | None = None,
        additionalMetricsToRetainV2: list[dict[str, Any]] | None = None,
        tags: list[dict[str, Any]] | None = None,
        metricsExportConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stream(
        self,
        *,
        streamId: str,
        files: list[dict[str, Any]],
        roleArn: str,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_thing(
        self,
        *,
        thingName: str,
        thingTypeName: str | None = None,
        attributePayload: dict[str, Any] | None = None,
        billingGroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_thing_group(
        self,
        *,
        thingGroupName: str,
        parentGroupName: str | None = None,
        thingGroupProperties: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_thing_type(
        self,
        *,
        thingTypeName: str,
        thingTypeProperties: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic_rule(
        self,
        *,
        ruleName: str,
        topicRulePayload: dict[str, Any],
        tags: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic_rule_destination(
        self,
        *,
        destinationConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_audit_configuration(
        self,
        *,
        deleteScheduledAudits: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_audit_suppression(
        self,
        *,
        checkName: str,
        resourceIdentifier: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_authorizer(
        self,
        *,
        authorizerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_billing_group(
        self,
        *,
        billingGroupName: str,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ca_certificate(
        self,
        *,
        certificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate(
        self,
        *,
        certificateId: str,
        forceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate_provider(
        self,
        *,
        certificateProviderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_command(
        self,
        *,
        commandId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_command_execution(
        self,
        *,
        executionId: str,
        targetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_metric(
        self,
        *,
        metricName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dimension(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_configuration(
        self,
        *,
        domainConfigurationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dynamic_thing_group(
        self,
        *,
        thingGroupName: str,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fleet_metric(
        self,
        *,
        metricName: str,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job(
        self,
        *,
        jobId: str,
        force: bool | None = None,
        namespaceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        executionNumber: int,
        force: bool | None = None,
        namespaceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job_template(
        self,
        *,
        jobTemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_mitigation_action(
        self,
        *,
        actionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ota_update(
        self,
        *,
        otaUpdateId: str,
        deleteStream: bool | None = None,
        forceDeleteAWSJob: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_package(
        self,
        *,
        packageName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_package_version(
        self,
        *,
        packageName: str,
        versionName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy(
        self,
        *,
        policyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy_version(
        self,
        *,
        policyName: str,
        policyVersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_provisioning_template(
        self,
        *,
        templateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_provisioning_template_version(
        self,
        *,
        templateName: str,
        versionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_registration_code(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_role_alias(
        self,
        *,
        roleAlias: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_scheduled_audit(
        self,
        *,
        scheduledAuditName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_profile(
        self,
        *,
        securityProfileName: str,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stream(
        self,
        *,
        streamId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_thing(
        self,
        *,
        thingName: str,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_thing_group(
        self,
        *,
        thingGroupName: str,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_thing_type(
        self,
        *,
        thingTypeName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic_rule(
        self,
        *,
        ruleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic_rule_destination(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_v2_logging_level(
        self,
        *,
        targetType: str,
        targetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprecate_thing_type(
        self,
        *,
        thingTypeName: str,
        undoDeprecate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_audit_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_audit_finding(
        self,
        *,
        findingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_audit_mitigation_actions_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_audit_suppression(
        self,
        *,
        checkName: str,
        resourceIdentifier: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_audit_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_authorizer(
        self,
        *,
        authorizerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_billing_group(
        self,
        *,
        billingGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ca_certificate(
        self,
        *,
        certificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificate(
        self,
        *,
        certificateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificate_provider(
        self,
        *,
        certificateProviderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_metric(
        self,
        *,
        metricName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_default_authorizer(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_detect_mitigation_actions_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dimension(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_configuration(
        self,
        *,
        domainConfigurationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_encryption_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint(
        self,
        *,
        endpointType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_event_configurations(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_metric(
        self,
        *,
        metricName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_index(
        self,
        *,
        indexName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job(
        self,
        *,
        jobId: str,
        beforeSubstitution: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        executionNumber: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job_template(
        self,
        *,
        jobTemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_managed_job_template(
        self,
        *,
        templateName: str,
        templateVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mitigation_action(
        self,
        *,
        actionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_provisioning_template(
        self,
        *,
        templateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_provisioning_template_version(
        self,
        *,
        templateName: str,
        versionId: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_role_alias(
        self,
        *,
        roleAlias: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduled_audit(
        self,
        *,
        scheduledAuditName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_profile(
        self,
        *,
        securityProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stream(
        self,
        *,
        streamId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_thing(
        self,
        *,
        thingName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_thing_group(
        self,
        *,
        thingGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_thing_registration_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_thing_type(
        self,
        *,
        thingTypeName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_policy(
        self,
        *,
        policyName: str,
        target: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_principal_policy(
        self,
        *,
        policyName: str,
        principal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_security_profile(
        self,
        *,
        securityProfileName: str,
        securityProfileTargetArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_thing_principal(
        self,
        *,
        thingName: str,
        principal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_topic_rule(
        self,
        *,
        ruleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_sbom_from_package_version(
        self,
        *,
        packageName: str,
        versionName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_topic_rule(
        self,
        *,
        ruleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_behavior_model_training_summaries(
        self,
        *,
        securityProfileName: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_buckets_aggregation(
        self,
        *,
        queryString: str,
        aggregationField: str,
        bucketsAggregationType: dict[str, Any],
        indexName: str | None = None,
        queryVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cardinality(
        self,
        *,
        queryString: str,
        indexName: str | None = None,
        aggregationField: str | None = None,
        queryVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_command(
        self,
        *,
        commandId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_command_execution(
        self,
        *,
        executionId: str,
        targetArn: str,
        includeResult: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_effective_policies(
        self,
        *,
        principal: str | None = None,
        cognitoIdentityPoolId: str | None = None,
        thingName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_indexing_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_document(
        self,
        *,
        jobId: str,
        beforeSubstitution: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_logging_options(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ota_update(
        self,
        *,
        otaUpdateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_package(
        self,
        *,
        packageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_package_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_package_version(
        self,
        *,
        packageName: str,
        versionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_percentiles(
        self,
        *,
        queryString: str,
        indexName: str | None = None,
        aggregationField: str | None = None,
        queryVersion: str | None = None,
        percents: list[float | int] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy(
        self,
        *,
        policyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy_version(
        self,
        *,
        policyName: str,
        policyVersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_registration_code(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_statistics(
        self,
        *,
        queryString: str,
        indexName: str | None = None,
        aggregationField: str | None = None,
        queryVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_thing_connectivity_data(
        self,
        *,
        thingName: str,
        includeSocketInformation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_topic_rule(
        self,
        *,
        ruleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_topic_rule_destination(
        self,
        *,
        arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_v2_logging_options(
        self,
        *,
        verbose: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_active_violations(
        self,
        *,
        thingName: str | None = None,
        securityProfileName: str | None = None,
        behaviorCriteriaType: str | None = None,
        listSuppressedAlerts: bool | None = None,
        verificationState: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attached_policies(
        self,
        *,
        target: str,
        recursive: bool | None = None,
        marker: str | None = None,
        pageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_audit_findings(
        self,
        *,
        taskId: str | None = None,
        checkName: str | None = None,
        resourceIdentifier: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        startTime: datetime.datetime | str | None = None,
        endTime: datetime.datetime | str | None = None,
        listSuppressedFindings: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_audit_mitigation_actions_executions(
        self,
        *,
        taskId: str,
        findingId: str,
        actionStatus: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_audit_mitigation_actions_tasks(
        self,
        *,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        auditTaskId: str | None = None,
        findingId: str | None = None,
        taskStatus: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_audit_suppressions(
        self,
        *,
        checkName: str | None = None,
        resourceIdentifier: dict[str, Any] | None = None,
        ascendingOrder: bool | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_audit_tasks(
        self,
        *,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        taskType: str | None = None,
        taskStatus: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_authorizers(
        self,
        *,
        pageSize: int | None = None,
        marker: str | None = None,
        ascendingOrder: bool | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_billing_groups(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        namePrefixFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ca_certificates(
        self,
        *,
        pageSize: int | None = None,
        marker: str | None = None,
        ascendingOrder: bool | None = None,
        templateName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificate_providers(
        self,
        *,
        nextToken: str | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificates(
        self,
        *,
        pageSize: int | None = None,
        marker: str | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificates_by_ca(
        self,
        *,
        caCertificateId: str,
        pageSize: int | None = None,
        marker: str | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_command_executions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        namespace: str | None = None,
        status: str | None = None,
        sortOrder: str | None = None,
        startedTimeFilter: dict[str, Any] | None = None,
        completedTimeFilter: dict[str, Any] | None = None,
        targetArn: str | None = None,
        commandArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_commands(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        namespace: str | None = None,
        commandParameterName: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_metrics(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_detect_mitigation_actions_executions(
        self,
        *,
        taskId: str | None = None,
        violationId: str | None = None,
        thingName: str | None = None,
        startTime: datetime.datetime | str | None = None,
        endTime: datetime.datetime | str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_detect_mitigation_actions_tasks(
        self,
        *,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dimensions(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_configurations(
        self,
        *,
        marker: str | None = None,
        pageSize: int | None = None,
        serviceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_fleet_metrics(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_indices(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_job_executions_for_job(
        self,
        *,
        jobId: str,
        status: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_job_executions_for_thing(
        self,
        *,
        thingName: str,
        status: str | None = None,
        namespaceId: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        jobId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_job_templates(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        status: str | None = None,
        targetSelection: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        thingGroupName: str | None = None,
        thingGroupId: str | None = None,
        namespaceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_managed_job_templates(
        self,
        *,
        templateName: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metric_values(
        self,
        *,
        thingName: str,
        metricName: str,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        dimensionName: str | None = None,
        dimensionValueOperator: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_mitigation_actions(
        self,
        *,
        actionType: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ota_updates(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        otaUpdateStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_outgoing_certificates(
        self,
        *,
        pageSize: int | None = None,
        marker: str | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_package_versions(
        self,
        *,
        packageName: str,
        status: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_packages(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies(
        self,
        *,
        marker: str | None = None,
        pageSize: int | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_principals(
        self,
        *,
        policyName: str,
        marker: str | None = None,
        pageSize: int | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_versions(
        self,
        *,
        policyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_principal_policies(
        self,
        *,
        principal: str,
        marker: str | None = None,
        pageSize: int | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_principal_things(
        self,
        *,
        principal: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_principal_things_v2(
        self,
        *,
        principal: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        thingPrincipalType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioning_template_versions(
        self,
        *,
        templateName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioning_templates(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_related_resources_for_audit_finding(
        self,
        *,
        findingId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_role_aliases(
        self,
        *,
        pageSize: int | None = None,
        marker: str | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sbom_validation_results(
        self,
        *,
        packageName: str,
        versionName: str,
        validationResult: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_scheduled_audits(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profiles(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        dimensionName: str | None = None,
        metricName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profiles_for_target(
        self,
        *,
        securityProfileTargetArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        recursive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_streams(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        ascendingOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_targets_for_policy(
        self,
        *,
        policyName: str,
        marker: str | None = None,
        pageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_targets_for_security_profile(
        self,
        *,
        securityProfileName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_groups(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        parentGroup: str | None = None,
        namePrefixFilter: str | None = None,
        recursive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_groups_for_thing(
        self,
        *,
        thingName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_principals(
        self,
        *,
        thingName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_principals_v2(
        self,
        *,
        thingName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        thingPrincipalType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_registration_task_reports(
        self,
        *,
        taskId: str,
        reportType: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_registration_tasks(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_thing_types(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        thingTypeName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_things(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        attributeName: str | None = None,
        attributeValue: str | None = None,
        thingTypeName: str | None = None,
        usePrefixAttributeValue: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_things_in_billing_group(
        self,
        *,
        billingGroupName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_things_in_thing_group(
        self,
        *,
        thingGroupName: str,
        recursive: bool | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topic_rule_destinations(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topic_rules(
        self,
        *,
        topic: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        ruleDisabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_v2_logging_levels(
        self,
        *,
        targetType: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_violation_events(
        self,
        *,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        thingName: str | None = None,
        securityProfileName: str | None = None,
        behaviorCriteriaType: str | None = None,
        listSuppressedAlerts: bool | None = None,
        verificationState: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_verification_state_on_violation(
        self,
        *,
        violationId: str,
        verificationState: str,
        verificationStateDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_ca_certificate(
        self,
        *,
        caCertificate: str,
        verificationCertificate: str | None = None,
        setAsActive: bool | None = None,
        allowAutoRegistration: bool | None = None,
        registrationConfig: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        certificateMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_certificate(
        self,
        *,
        certificatePem: str,
        caCertificatePem: str | None = None,
        setAsActive: bool | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_certificate_without_ca(
        self,
        *,
        certificatePem: str,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_thing(
        self,
        *,
        templateBody: str,
        parameters: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_certificate_transfer(
        self,
        *,
        certificateId: str,
        rejectReason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_thing_from_billing_group(
        self,
        *,
        billingGroupName: str | None = None,
        billingGroupArn: str | None = None,
        thingName: str | None = None,
        thingArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_thing_from_thing_group(
        self,
        *,
        thingGroupName: str | None = None,
        thingGroupArn: str | None = None,
        thingName: str | None = None,
        thingArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_topic_rule(
        self,
        *,
        ruleName: str,
        topicRulePayload: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_index(
        self,
        *,
        queryString: str,
        indexName: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        queryVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_default_authorizer(
        self,
        *,
        authorizerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_default_policy_version(
        self,
        *,
        policyName: str,
        policyVersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_logging_options(
        self,
        *,
        loggingOptionsPayload: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_v2_logging_level(
        self,
        *,
        logTarget: dict[str, Any],
        logLevel: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_v2_logging_options(
        self,
        *,
        roleArn: str | None = None,
        defaultLogLevel: str | None = None,
        disableAllLogs: bool | None = None,
        eventConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_audit_mitigation_actions_task(
        self,
        *,
        taskId: str,
        target: dict[str, Any],
        auditCheckToActionsMapping: dict[str, list[str]],
        clientRequestToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_detect_mitigation_actions_task(
        self,
        *,
        taskId: str,
        target: dict[str, Any],
        actions: list[str],
        clientRequestToken: str,
        violationEventOccurrenceRange: dict[str, Any] | None = None,
        includeOnlyActiveViolations: bool | None = None,
        includeSuppressedAlerts: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_on_demand_audit_task(
        self,
        *,
        targetCheckNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_thing_registration_task(
        self,
        *,
        templateBody: str,
        inputFileBucket: str,
        inputFileKey: str,
        roleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_thing_registration_task(
        self,
        *,
        taskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_authorization(
        self,
        *,
        authInfos: list[dict[str, Any]],
        principal: str | None = None,
        cognitoIdentityPoolId: str | None = None,
        clientId: str | None = None,
        policyNamesToAdd: list[str] | None = None,
        policyNamesToSkip: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_invoke_authorizer(
        self,
        *,
        authorizerName: str,
        token: str | None = None,
        tokenSignature: str | None = None,
        httpContext: dict[str, Any] | None = None,
        mqttContext: dict[str, Any] | None = None,
        tlsContext: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transfer_certificate(
        self,
        *,
        certificateId: str,
        targetAwsAccount: str,
        transferMessage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_audit_configuration(
        self,
        *,
        roleArn: str | None = None,
        auditNotificationTargetConfigurations: dict[str, dict[str, Any]] | None = None,
        auditCheckConfigurations: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_audit_suppression(
        self,
        *,
        checkName: str,
        resourceIdentifier: dict[str, Any],
        expirationDate: datetime.datetime | str | None = None,
        suppressIndefinitely: bool | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_authorizer(
        self,
        *,
        authorizerName: str,
        authorizerFunctionArn: str | None = None,
        tokenKeyName: str | None = None,
        tokenSigningPublicKeys: dict[str, str] | None = None,
        status: str | None = None,
        enableCachingForHttp: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_billing_group(
        self,
        *,
        billingGroupName: str,
        billingGroupProperties: dict[str, Any],
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ca_certificate(
        self,
        *,
        certificateId: str,
        newStatus: str | None = None,
        newAutoRegistrationStatus: str | None = None,
        registrationConfig: dict[str, Any] | None = None,
        removeAutoRegistration: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_certificate(
        self,
        *,
        certificateId: str,
        newStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_certificate_provider(
        self,
        *,
        certificateProviderName: str,
        lambdaFunctionArn: str | None = None,
        accountDefaultForOperations: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_command(
        self,
        *,
        commandId: str,
        displayName: str | None = None,
        description: str | None = None,
        deprecated: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_custom_metric(
        self,
        *,
        metricName: str,
        displayName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dimension(
        self,
        *,
        name: str,
        stringValues: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_configuration(
        self,
        *,
        domainConfigurationName: str,
        authorizerConfig: dict[str, Any] | None = None,
        domainConfigurationStatus: str | None = None,
        removeAuthorizerConfig: bool | None = None,
        tlsConfig: dict[str, Any] | None = None,
        serverCertificateConfig: dict[str, Any] | None = None,
        authenticationType: str | None = None,
        applicationProtocol: str | None = None,
        clientCertificateConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dynamic_thing_group(
        self,
        *,
        thingGroupName: str,
        thingGroupProperties: dict[str, Any],
        expectedVersion: int | None = None,
        indexName: str | None = None,
        queryString: str | None = None,
        queryVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_encryption_configuration(
        self,
        *,
        encryptionType: str,
        kmsKeyArn: str | None = None,
        kmsAccessRoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_event_configurations(
        self,
        *,
        eventConfigurations: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_fleet_metric(
        self,
        *,
        metricName: str,
        indexName: str,
        queryString: str | None = None,
        aggregationType: dict[str, Any] | None = None,
        period: int | None = None,
        aggregationField: str | None = None,
        description: str | None = None,
        queryVersion: str | None = None,
        unit: str | None = None,
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_indexing_configuration(
        self,
        *,
        thingIndexingConfiguration: dict[str, Any] | None = None,
        thingGroupIndexingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_job(
        self,
        *,
        jobId: str,
        description: str | None = None,
        presignedUrlConfig: dict[str, Any] | None = None,
        jobExecutionsRolloutConfig: dict[str, Any] | None = None,
        abortConfig: dict[str, Any] | None = None,
        timeoutConfig: dict[str, Any] | None = None,
        namespaceId: str | None = None,
        jobExecutionsRetryConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_mitigation_action(
        self,
        *,
        actionName: str,
        roleArn: str | None = None,
        actionParams: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package(
        self,
        *,
        packageName: str,
        description: str | None = None,
        defaultVersionName: str | None = None,
        unsetDefaultVersion: bool | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package_configuration(
        self,
        *,
        versionUpdateByJobsConfig: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_package_version(
        self,
        *,
        packageName: str,
        versionName: str,
        description: str | None = None,
        attributes: dict[str, str] | None = None,
        artifact: dict[str, Any] | None = None,
        action: str | None = None,
        recipe: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_provisioning_template(
        self,
        *,
        templateName: str,
        description: str | None = None,
        enabled: bool | None = None,
        defaultVersionId: int | None = None,
        provisioningRoleArn: str | None = None,
        preProvisioningHook: dict[str, Any] | None = None,
        removePreProvisioningHook: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_role_alias(
        self,
        *,
        roleAlias: str,
        roleArn: str | None = None,
        credentialDurationSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_scheduled_audit(
        self,
        *,
        scheduledAuditName: str,
        frequency: str | None = None,
        dayOfMonth: str | None = None,
        dayOfWeek: str | None = None,
        targetCheckNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_profile(
        self,
        *,
        securityProfileName: str,
        securityProfileDescription: str | None = None,
        behaviors: list[dict[str, Any]] | None = None,
        alertTargets: dict[str, dict[str, Any]] | None = None,
        additionalMetricsToRetain: list[str] | None = None,
        additionalMetricsToRetainV2: list[dict[str, Any]] | None = None,
        deleteBehaviors: bool | None = None,
        deleteAlertTargets: bool | None = None,
        deleteAdditionalMetricsToRetain: bool | None = None,
        expectedVersion: int | None = None,
        metricsExportConfig: dict[str, Any] | None = None,
        deleteMetricsExportConfig: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stream(
        self,
        *,
        streamId: str,
        description: str | None = None,
        files: list[dict[str, Any]] | None = None,
        roleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_thing(
        self,
        *,
        thingName: str,
        thingTypeName: str | None = None,
        attributePayload: dict[str, Any] | None = None,
        expectedVersion: int | None = None,
        removeThingType: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_thing_group(
        self,
        *,
        thingGroupName: str,
        thingGroupProperties: dict[str, Any],
        expectedVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_thing_groups_for_thing(
        self,
        *,
        thingName: str | None = None,
        thingGroupsToAdd: list[str] | None = None,
        thingGroupsToRemove: list[str] | None = None,
        overrideDynamicGroups: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_thing_type(
        self,
        *,
        thingTypeName: str,
        thingTypeProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic_rule_destination(
        self,
        *,
        arn: str,
        status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_security_profile_behaviors(
        self,
        *,
        behaviors: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
