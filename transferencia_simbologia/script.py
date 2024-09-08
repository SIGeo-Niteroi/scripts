'''
Código para transferir uma simbologia de uma camada em um webmap para uma camada hospedada
'''

import ast
import os
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from dotenv import load_dotenv

# Carrega o arquivo de variáveis de ambiente
load_dotenv() 
USER_NAME = os.getenv('APP_USER_NAME')
PASSWORD = os.getenv('APP_PASSWORD')
PORTAL = os.getenv('APP_PORTAL')
WEBMAP = os.getenv('WEBMAP_ITEM')
LAYER = os.getenv('LAYER_ITEM')
INDEX = os.getenv('LAYER_INDEX')

# Conexão com o arcgisonline
gis = GIS(PORTAL, username=USER_NAME, password=PASSWORD)

# Consulta os dados do webmap
wm_item = gis.content.get(WEBMAP)
webmap = wm_item.get_data()

# Consulta a simbologia da camada no webmap
operational_layers = webmap['operationalLayers'][INDEX]
symbol = operational_layers['drawingInfo']['renderer']

# Consulta a camada a partir do item
lyr_item = gis.content.get(LAYER)
layer = FeatureLayer.fromitem(lyr_item)

# Tratamento de dados
drawinginfo = '{"drawingInfo":{"renderer":' + str(symbol) + '}}'
data_update = ast.literal_eval(drawinginfo)

# Atualiza a camada com os dados de simbologia   
layer.manager.update_definition(data_update)
