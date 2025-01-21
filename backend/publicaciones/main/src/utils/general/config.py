import configparser
import os

CFG = configparser.ConfigParser()
config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
CFG.read(config_path, encoding='utf-8')

AMBIENTE = CFG.get('AMBIENTE', 'env')

class Parametros:
    db_user = CFG[AMBIENTE]['db_user']
    db_pass = CFG[AMBIENTE]['db_pass']
    db_host = CFG[AMBIENTE]['db_host']
    db_name = CFG[AMBIENTE]['db_name']
    db_port = CFG[AMBIENTE]['db_port']
    secret_jwt = CFG[AMBIENTE]['secret_jwt']


