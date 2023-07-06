import re

class extractorURL:
    def __init__(self, url):
        self.url = self.verify_url_type(url)
        self.validate_url()

    def verify_url_type(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def validate_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        
        pattern_URL = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = pattern_URL.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_base_url(self):
        index = self.url.find('?')
        base_URL = self.url[:index]
        return base_URL

    def get_url_params(self):
        index = self.url.find('?')
        params_URL = self.url[index+1:]
        return params_URL
    
    def get_param_value(self, param):
        index = self.get_url_params().find(param)
        index_value = index + len(param) + 1
        index_e = self.get_url_params().find('&', index_value)
        if index_e == -1:
            value = self.get_url_params()[index_value:]
        else:
            value = self.get_url_params()[index_value:index_e]
        return value

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_params() + "\n" + "URL Base: " + self.get_base_url()
    
    def __eq__(self, other):
        return self.url == other.url
