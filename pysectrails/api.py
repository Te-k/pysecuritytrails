import requests


class SecurityTrailsError(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, message)


class SecurityTrails(object):
    def __init__(self, key):
        self.api_key = key
        self.base_url = "https://api.securitytrails.com/v1/"

    def _request(self, path, params={}):
        headers = {'APIKEY': self.api_key}
        r = requests.get(self.base_url + path, params=params, headers=headers)
        if r.status_code != 200:
            raise SecurityTrailsError('Bad HTTP Status Code %i' % r.status_code)
        return r.json()

    def ping(self):
        return self._request('ping')

    def usage(self):
        return self._request('account/usage')

    def domain_info(self, domain):
        return self._request('domain/' + domain)

    def domain_subdomains(self, domain):
        return self._request('domain/' + domain + '/subdomains')

    def domain_tags(self, domain):
        return self._request('domain/' + domain + '/tags')

    def domain_whois(self, domain):
        return self._request('domain/' + domain + '/whois')

    def domain_history_dns(self, domain, type='a'):
        if type not in ['a', 'aaaa', 'soa', 'mx', 'ns', 'txt']:
            raise SecurityTrailsError('Invalid DNS type given')
        res = self._request('history/' + domain + '/dns/' + type)
        if res['pages'] > 1:
            for page in range(2, res['pages']):
                params = {'page': page}
                temp_res = self._request(
                    'history/' + domain + '/dns/' + type,
                    params=params
                )
                res['records'].extend(temp_res['records'])
        return res

    def domain_history_whois(self, domain):
        # TODO: implement pagination here
        return self._request('history/' + domain + '/whois')
