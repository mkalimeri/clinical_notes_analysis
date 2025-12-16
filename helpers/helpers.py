from dotenv import load_dotenv
from environs import Env
import logging
import os
from typing import Dict, Tuple


def get_environment_variables(env: Env) -> Tuple:
    """
    Get the AWS credentials from the .env file
    :param env: os.environ, the environment the variables will be extracted from
    :return: Tuple, tuple of dictionary containing the credentials for AWS, InfluxDB and Elastic Cloud
    """
    try:
        logging.info(f"Loading environment variables")
        load_dotenv()

        aws_storage_options = {}

        aws_storage_options["key"] = os.getenv("AWS_ACCESS_KEY_ID")
        aws_storage_options["secret"] = os.getenv("AWS_SECRET_ACCESS_KEY")

        return aws_storage_options
    except Exception as e:
        logging.exception(f"Could not load environment variables: {e}")
