import logging

from .sts import SessionHelper

log = logging.getLogger(__name__)


class KMS:
    @staticmethod
    def put_key_policy(
        account_id: str,
        key_id: str,
        policy_name: str,
        policy: str,
    ):
        try:
            aws_session = SessionHelper.remote_session(accountid=account_id)
            kms_client = aws_session.client('kms')
            kms_client.put_key_policy(
                KeyId=key_id,
                PolicyName=policy_name,
                Policy=policy,
            )
        except Exception as e:
            log.error(
                f'Failed to attach policy to KMS key {key_id} on {account_id} : {e} '
            )
            raise e

    @staticmethod
    def get_key_policy(
        account_id: str,
        key_id: str,
        policy_name: str,
    ):
        try:
            aws_session = SessionHelper.remote_session(accountid=account_id)
            kms_client = aws_session.client('kms')
            response = kms_client.get_key_policy(
                KeyId=key_id,
                PolicyName=policy_name,
            )
            return response['Policy']
        except Exception:
            return None

    @staticmethod
    def get_key_id(
        account_id: str,
        key_alias: str,
    ):
        try:
            aws_session = SessionHelper.remote_session(accountid=account_id)
            kms_client = aws_session.client('kms')
            response = kms_client.describe_key(
                KeyId=key_alias,
            )
            return response['KeyMetadata']['KeyId']
        except Exception:
            return None
