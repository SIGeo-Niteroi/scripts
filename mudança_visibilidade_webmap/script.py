'''
Código para deixar a visibilidade das camadas de um webmap desligada
'''
import json
import os
from dotenv import load_dotenv
from arcgis.gis import GIS
from arcgis.mapping import WebMap

# Carrega o arquivo de variáveis de ambiente
load_dotenv() 
USER_NAME = os.getenv('APP_USER_NAME')
PASSWORD = os.getenv('APP_PASSWORD')
PORTAL = os.getenv('APP_PORTAL')
WEBMAP = os.getenv('WEBMAP_ITEM')

# Conexão com o arcgisonline
gis = GIS(PORTAL, username=USER_NAME, password=PASSWORD)

# Consulta os dados do webmap
wm_item = gis.content.get(WEBMAP)
webmap = wm_item.get_data()

# Listagem das camadas do webmap
operational_layers = webmap['operationalLayers']

# Desliga a visibilidade das camadas
for lyr in operational_layers:
    lyr['visibility'] = False

# Atualiza o webmap
item_properties = {"text": json.dumps(webmap)}
wm_item.update(item_properties=item_properties)
wm = WebMap(wm_item)

