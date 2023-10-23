import json
import sys

def _load_json_data(input_file):
    try:
        with open(input_file, 'r') as input_json:
            json_data = json.load(input_json)
        return json_data
    except Exception as e:
        print("Input file Error! {}".format(e))
        return sys.exit(2)

def semistruct_to_pgraph(in_file, mapcfg_file, out_file='./pgraph.json', debug=False):

    if debug:
        print('input file = {}, mapping configuration file = {}, \
               output file = {}'.format(in_file, mapcfg_file, out_file))

    # Read file input file containing JSON format 
    #semi-structured data and mapping configuration file in JSON format

    source_data = _load_json_data(in_file)
    mapping_config = _load_json_data(mapcfg_file)

    if debug:
        print("input data:")
        print(source_data)
        print("mapping configuration:")
        print(mapping_config)

    # Initialize the property graph
    property_graph = {
        "graph": {
            "nodes": [],
            "edges": []
        }
    }

    # Add nodes to the property graph
    for i in range(len(mapping_config['schema-map']['nodes'])):
        for element in source_data[mapping_config['schema-map']['nodes'][i]['label']]:
            node = {
                "node": {
                    "id": element[mapping_config['schema-map']['nodes'][i]['node-id']],
                    "label": mapping_config['schema-map']['nodes'][i]['label'],
                    "properties": {}  # mapping_config['schema-map']['nodes'][i]['node-properties']
                }
            }

            # Map properties to the node
            for property_name, property_mapping in mapping_config['schema-map']['nodes'][i]['node-properties'].items():
                # Assuming property_mapping is a dictionary
                data_value = property_mapping.get("data_value", None)
                data_type = property_mapping.get("data_type", None)

                # Now, you can split the data_value (assuming it's a string)
                if data_value is not None:
                    for key in data_value.split('.'):
                        property_value = element.get(key, None)
                        if property_value is None:
                            break

                if property_value is not None:
                    node["node"]["properties"][property_name] = {
                        "datatype": data_type,  # comment: modify this based on the actual data types
                        "data value": property_value
                    }

            property_graph["graph"]["nodes"].append(node)

    # Create edges
    # Inefficient currently - goes through source and target node lists and matches individually
    for edge in mapping_config['schema-map']['edges']:
        src_type = edge['_source_type']
        trgt_type = edge['_target_type']
        src_match = edge['_source']
        trgt_match = edge['_target']
        src_nodes = []
        target_nodes = []
        for node in property_graph['graph']['nodes']:
            if node['node']['label'] == src_type:
                src_nodes.append(node)
            if node['node']['label'] == trgt_type:
                target_nodes.append(node)
        edge_id = 0
        for s_node in src_nodes:
            for t_node in target_nodes:
                if t_node['node']['properties'][trgt_match]['datatype'] == 'list':
                    if s_node['node'][src_match] in t_node['node']['properties'][trgt_match]['data value']:
                        edge_node = {
                            "edge": {
                                "id": len(property_graph["graph"]["edges"]) + 1,
                                # "relationship": mapping_config['schema-map']['edges'][edge_node]['relationship'],
                                "from_node_id": s_node['node']['id'],
                                "to_node_id": t_node['node']['id'],
                                "properties": {}
                            }
                        }
                        property_graph["graph"]["edges"].append(edge_node)

                elif s_node['node'][src_match] == t_node['node']['properties'][trgt_match]['data value']:
                    edge_node = {
                        "edge": {
                            "id": len(property_graph["graph"]["edges"]) + 1,
                            # "relationship": mapping_config['schema-map']['edges'][edge_node]['relationship'],
                            "from_node_id": s_node['node']['id'],
                            "to_node_id": t_node['node']['id'],
                            "properties": {}
                        }
                    }

                    property_graph["graph"]["edges"].append(edge_node)

    # Save the property graph in JSON format
    if debug:
        print("generated property graph:")
        print(property_graph)
    with open(out_file, "w") as output_file:
        json.dump(property_graph, output_file, indent=4)

    return

