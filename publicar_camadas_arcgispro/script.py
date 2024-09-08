'''
Código para publicar camadas de um geodatabase no ArcGIS Pro como camadas hospedadas
'''

def share_web_layer(feature_dataset, layer_name, share_file):
    
    '''
    Código para publicar camadas de um geodatabase no ArcGIS Pro como camadas hospedadas
    feature_dataset: str - caminho do feature dataset
    layer_name: str - nome desejado para salvar a camada
    share_file: str - caminho para salvar o arquivo de rascunho e publicação ex: "Documents/Publicacao/nome_camada"
    '''
    import arcpy
    import time
    
    # Projeto 
    begin = time.time()
    project = arcpy.mp.ArcGISProject('CURRENT')
    m = project.listMaps("Map")[0] 

    # Adiciona as camadas do feature dataset no mapa
    m.addDataFromPath(feature_dataset)
    project.save()

    # Publica o feature dataset
    
    feature_dataset = m.getWebLayerSharingDraft('HOSTING_SERVER','FEATURE', layer_name)
    feature_dataset.exportToSDDraft(f'{share_file}.sddraft')
    

    arcpy.server.StageService(f'{share_file}.sddraft', f'{share_file}.sd')
    arcpy.server.UploadServiceDefinition(f'{share_file}.sd', 'HOSTING_SERVER')

    end = time.time()
    print(f'Tempo de criação do serviço: {end-begin}')
