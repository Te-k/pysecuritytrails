# pysectrails

Python3 wrapper for the Security Trails API https://securitytrails.com/

## Installation

```
git clone https://github.com/Te-k/pysectrails.git
cd pysectrails
pip install .
```

## Usage

```py
from pysectrails import SecurityTrails, SecurityTrailsError
st = SecurityTrails('APIKEYHERE')

# Check that it is working
try:
    st.ping()
except SecurityTrailsError:
    print('Ping failed')
    sys.exit(1)

infos = st.domain_info('securitytrails.com')
subdomains = st.domain_subdomains('securitytrails.com')
tags = st.domain_tags('securitytrails.com')
whois = st.domain_whois('securitytrails.com')
history_dns = st.domain_history_dns('securitytrails.com')
history_whois = st.domain_history_whois('securitytrails.com')
```

For more information on the API, check https://securitytrails.com/corp/apidocs

## License

This code is licensed under GPLv3
