# pysecuritytrails

Python3 wrapper for the Security Trails API https://securitytrails.com/

## Installation

You can install it directly from the [pypi](https://pypi.org/project/pysecuritytrails/) package : `pip install pysecuritytrails`

You can also install the last version of the source code:

```
git clone https://github.com/Te-k/pysecuritytrails.git
cd pysecuritytrails
pip install .
```

## Usage

```py
from pysecuritytrails import SecurityTrails, SecurityTrailsError
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

For more information on the API, check https://docs.securitytrails.com/reference

## List of Functions Implemented

* `ping()`: [You can use this simple endpoint to test your authentication and access to the SecurityTrails API.](https://docs.securitytrails.com/v1.0/reference#ping)
* `scroll(scroll_id)`: [A fast and easy way to fetch many results](https://docs.securitytrails.com/v1.0/reference#scroll)
* `domain_info(HOSTNAME)`: [Returns the current data about the given domain.](https://docs.securitytrails.com/v1.0/reference#get-domain)
* `domain_subdomains(HOSTNAME)`: [Returns subdomains for a given hostname](https://docs.securitytrails.com/v1.0/reference#list-subdomains)
* `domain_tags(HOSTNAME)`: [Returns tags for a given hostname](https://docs.securitytrails.com/v1.0/reference#list-tags)
* `domain_associated(HOSTNAME, PAGE)`: [Find all domains that are related to a domain you input](https://docs.securitytrails.com/v1.0/reference#find-associated-domains)
* `domain_whois(HOSTNAME)`: [Returns the current WHOIS data about a given domain with the stats merged together](https://docs.securitytrails.com/v1.0/reference#get-whois)
* `domain_search(FILTER, INCLUDE_IPS, PAGE)` : [Filter and search specific records using this endpoint.](https://docs.securitytrails.com/reference#search)
* `domain_search_sql(QUERY, INCLUDE_IPS, PAGE, SCROLL)`: [Filter and search specific records using our DSL with this endpoint](https://docs.securitytrails.com/v1.0/reference#search)
* `domain_search_stats(FILTER)` : [Show statistics of a research](https://docs.securitytrails.com/reference#search-count)
* `domain_history_dns(HOSTNAME, TYPE, PAGE)`: [Lists out specific historical information about the given hostname parameter](https://docs.securitytrails.com/v1.0/reference#dns-history-by-record-type)
* `ips_nearby(IP)`: [Returns the neighbors in any given IP level range and essentially allows you to explore closeby IP addresses.](https://docs.securitytrails.com/v1.0/reference#ips)
* `ips_search_dsl(IP, PAGE)`: [Search for an IP address using DSL](https://docs.securitytrails.com/v1.0/reference#search-ips-dsl)
* `ips_search_stats(QUERY)`: [Stats on a DSL query](https://docs.securitytrails.com/v1.0/reference#ip-search-statistics)
* `feeds_domains(TYPE, FILTER, TLD, NS)`: [Fetch zone files including authoritative nameservers with ease](https://docs.securitytrails.com/v1.0/reference#feeds)

## License

This code is licensed under GPLv3
