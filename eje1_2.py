from db_functions import *
import json



if __name__ == "__main__":
    driver = openConnection()
    driver.verify_connectivity()



    with open('data.json', 'r') as archivo:
        data = json.load(archivo)
        print(data)


        try:

            print('Generando grafo...')

            # Crear nodos
            for node in data["nodes"]:
                createNode(driver, node["labels"], node["properties"])

            # Crear relaciones
            for relation in data["relations"]:
                createRelation(driver, label_1=relation["label1"], properties_1=relation["properties1"],
                                label_2=relation["label2"], properties_2=relation["properties2"],
                                relationType=relation["type"], relationProperties=relation["relProperties"])

            print("Buscar nodos: ")
            print(find_node(driver, ["Person", "Director"], {"name":"Juan"}))

            print("\nBuscar nodos con relaciones: ")
            res = find_node_with_relation(driver, ["Actor", "Director"], {}, "Movie", {"year":"1997"}, "ACTED_IN", {"role":"Jack Dawson"})
            print(res)

        except Exception as e:
            print(e)
        finally:
            closeConnection(driver)