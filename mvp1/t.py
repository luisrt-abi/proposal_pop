from collections import namedtuple

token_requirements = namedtuple('token_req', ['TOKENGEN_CLIENT_ID', 'TOKENGEN_CLIENT_SECRET', 'RECOMM_URL','TOKENGEN_URL'])

country_tokens = dict()
country_tokens['CO'] = token_requirements(TOKENGEN_CLIENT_ID='CO_ID', TOKENGEN_CLIENT_SECRET='CO_SECRET', RECOMM_URL='CO_RECOMM_URL', TOKENGEN_URL='CO_TOKENGEN_URL')
country_tokens['MX'] = token_requirements(TOKENGEN_CLIENT_ID='MX_ID', TOKENGEN_CLIENT
_SECRET='MX_SECRET', RECOMM_URL='MX_RECOMM_URL', TOKENGEN_URL='MX_TOKENGEN_URL')
country_tokens['default'] = token_requirements(TOKENGEN_CLIENT_ID='def_id', TOKENGEN_CLIENT_SECRET='def
