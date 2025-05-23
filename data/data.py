from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

class Anagrafica:
    def __init__(self, config: ConfigParser = config):
        self.data = config['anagrafica']

    @property
    def nome(self): return self.data.get("NOME", "")
    @property
    def cognome(self): return self.data.get("COGN", "")
    @property
    def codfisc(self): return self.data.get("CODFISC", "")
    @property
    def giorno(self): return self.data.get("GIORNO", "")
    @property
    def mese(self): return self.data.get("MESE", "")
    @property
    def anno(self): return self.data.get("ANNO", "")
    @property
    def luogo(self): return self.data.get("LUOGO", "")
    @property
    def prov(self): return self.data.get("PROV", "")
    @property
    def stato(self): return self.data.get("STATO", "")
    @property
    def cittadinanza(self): return self.data.get("CITIZ", "")


class Residenza:
    def __init__(self, config: ConfigParser = config):
        self.data = config['residenza']

    @property
    def via(self): return self.data.get("VIA", "")
    @property
    def num_civ(self): return self.data.get("NUM_CIV", "")
    @property
    def cap(self): return self.data.get("CAP", "")
    @property
    def citta(self): return self.data.get("CITTA", "")
    @property
    def prov(self): return self.data.get("PROV", "")
    @property
    def stato(self): return self.data.get("STATO", "")
    @property
    def telefono(self): return self.data.get("NUM", "")
    @property
    def email(self): return self.data.get("EMAIL", "")

class Professione:
    def __init__(self, config: ConfigParser = config):
        self.data = config['professione']

    @property
    def lavoro(self): return self.data.get("LAVORO", "")
    @property
    def tipo_scuola_attuale(self): return self.data.get("TIPO_SCUOLA_ATTUALE", "")
    @property
    def nome_scuola_attuale(self): return self.data.get("NOME_SCUOLA_ATTUALE", "")
    @property
    def tipo_scuola_titolo(self): return self.data.get("TIPO_SCUOLA_TITOLO", "")
    @property
    def nome_scuola_titolo(self): return self.data.get("NOME_SCUOLA_TITOLO", "")
    @property
    def data_titolo(self): return self.data.get("DATA_TITOLO", "")


class Famiglia:
    def __init__(self, config: ConfigParser = config):
        self.membri = []
        if 'famiglia' in config:
            famiglia_section = config['famiglia']
            for key in famiglia_section:
                parti = [x.strip() for x in famiglia_section[key].split(',')]
                if len(parti) == 4:
                    self.membri.append({
                        'nome': parti[0],
                        'data_nascita': parti[1],
                        'luogo_nascita': parti[2],
                        'parentela': parti[3]
                    })

class Banca:
    def __init__(self, config: ConfigParser = config):
        self.data = config['banca']
    
    @property
    def nome(self): return self.data.get("NOME", "")
    @property
    def iban(self): return self.data.get("IBAN", "")