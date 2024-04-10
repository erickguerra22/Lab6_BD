from neo4j import GraphDatabase

'''
    Funciones para creacion de grafos en Neo4j
    Autores:
        José Pablo Kiesling Lange - 21581
        Diego Andrés Morales Aquino - 21762
        Pablo Andrés Zamora Vásquez - 21780
        Elías Alberto Alvarado Raxón - 21808
        Erick Stiv Junior Guerra Muñoz - 21781
'''

# Variables globales
uri = "neo4j+ssc://9a670284.databases.neo4j.io"
user = "neo4j"
password = "q341vIR2TmgIvedPcx_pl3m5Y9B7ab-tTiBmY7cIEek"

def formatDict(dictionary):
    result = ', '.join(["{}: '{}'".format(k, str(v).replace("'", "\\'")) for k, v in dictionary.items()])
    return result


# Funciones
def openConnection():
    return GraphDatabase.driver(uri, auth=(user, password))

def closeConnection(driver):
    driver.close()
    
def createNode(driver, labels, properties):
    session = driver.session()
    if type(labels) == str:
        labels = [labels]
    try:
        labels_str = ":".join(labels)
        query = f"MERGE (n:{labels_str} {{{formatDict(properties)}}})"
        result = session.run(query)
        return result
    except Exception as e:
        print(labels, properties)
        print('¡Error al crear nodo! ', e)
    finally:
        session.close()
        
def find_node(driver, label, properties):
    session = driver.session()
    try:

        if type(label) == str:
            label = [label]
        labels_str = ":".join(label)
        properties_str = formatDict(properties)
        query = f"MATCH (n:{labels_str} {{{properties_str}}}) RETURN n" if properties else f"MATCH (n:{labels_str}) RETURN n"
        
        result = session.run(query)
        return [record.data() for record in result]

    except Exception as e:
        print('¡Error al buscar nodos!')
    finally:
        session.close()


def find_node_with_relation(driver, label_1, properties_1, label_2, properties_2, relationType, relationProperties):
    session = driver.session()
    try:
        if type(label_1) == str:
            label_1 = [label_1]
        if type(label_2) == str:
            label_2 = [label_2]

        label1_str = ":".join(label_1)
        label2_str = ":".join(label_2)
        
        query = f"""
        MATCH (n:{label1_str} {{{formatDict(properties_1)}}})
        -[r:{relationType} {{{formatDict(relationProperties)}}}]->
        (m:{label2_str} {{{formatDict(properties_2)}}})
        RETURN n,r,m
        """
        query = query.strip()
        result = session.run(query)
        return [record.data() for record in result]
    except Exception as e:
        print('¡Error al buscar nodos con relaciones!')
    finally:
        session.close()


    
def createRelation(driver, label_1, properties_1, label_2, properties_2, relationType, relationProperties):
    session = driver.session()
    try:
        query = f"""
                MATCH (n1:{label_1} {{{formatDict(properties_1)}}})
                MATCH (n2:{label_2} {{{formatDict(properties_2)}}})
                MERGE (n1)-[r:{relationType} {{{formatDict(relationProperties)}}}]->(n2)
                RETURN r
                """
        result = session.run(query)
        return result
    except Exception as e:
        print('¡Error al crear relación!')
    finally:
        session.close()
    