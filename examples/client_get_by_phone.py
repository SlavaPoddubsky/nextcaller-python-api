import logging
from requests import HTTPError, RequestException
from pynextcaller.client import NextCallerClient

logger = logging.getLogger('nextcaller')
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

username = 'XXXXX'
password = 'XXXXX'
sandbox = True
phone_number = '1211211212'
profile_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = NextCallerClient(username, password, sandbox=sandbox)

# get by phone
try:
    response_content = client.get_by_phone(phone_number, debug=True)
    logger.info(response_content)
except ValueError as err:
    logger.error('Validation Error: {}'.format(err))
except HTTPError as err:
    response = err.response
    response_code = response.status_code
    # try to parse error json message
    try:
        response_message = response.json()
    except (ValueError, TypeError):
        response_message = response.text
    logger.error(
        'HTTPError. Status code {}. Response message: {}'.
        format(response_code, response_message))
except RequestException as err:
    logger.error('RequestException. {}'.format(err))