import json
import sys

def _load_json_data(input_file):
   try:
      with open(input_file,'r') as input_json:
         json_data = json.load(input_json)
      return json_data
   except Exception as e:
      print("Input file Error! {}".format(e) )
      return sys.exit(2)


def semistruct_to_pgraph(in_file, mapcfg_file, out_file='./pgraph.json',debug=False):

   if debug:
      print('input file = {}, mapping configuration file = {}, output file = {}'.format(in_file, mapcfg_file, out_file))

   # read file input file containing json format semi-structured data 
   # and mapping configuraton file in json format
      
   source_data = _load_json_data(in_file)
   mapping_config = _load_json_data(mapcfg_file)
   if debug:
      print("input data:")
      print(source_data)
      print("mapping configuration :")
      print(mapping_config)

   # Initialize the property graph
   property_graph = {
      "graph": {
         "nodes": [],
         "edges": []
      }
   }

   # add nodes to the property graph
   for element in source_data[mapping_config['schema-map']['nodes'][0]['label']]:
      node = {
         "node": {
            "id": element[mapping_config['schema-map']['nodes'][0]['node-id']],
            "label": mapping_config['schema-map']['nodes'][0]['label'],
            "properties":{} #mapping_config['schema-map']['nodes'][0]['node-properties']
         }
      }

      # Map properties to the node
      for property_name, property_mapping in mapping_config['schema-map']['nodes'][0]['node-properties'].items():
         property_value = element
         for key in property_mapping.split('.'):
            property_value = property_value.get(key, None)
            if property_value is None:
               break

         if property_value is not None:
            node["node"]["properties"][property_name] = {
            "datatype": "string",  # comment : modify this based on the actual data types
            "data value": property_value
            }

      property_graph["graph"]["nodes"].append(node)
    

   # source data and add edges to the property graph
   for element in source_data[mapping_config['schema-map']['nodes'][0]['label']]:
      source_id = element[mapping_config['schema-map']['nodes'][0]['node-id']]
      target = element.get(mapping_config['schema-map']['edges'][0]['edge-type'], [])

      for target_id in target:
         edge = {
            "edge": {
               "id": len(property_graph["graph"]["edges"]) + 1,
               "relationship": mapping_config['schema-map']['edges'][0]['relationship'],
               "from_node_id": source_id,
               "to_node_id": target_id,
               "properties": {}
            }
         }

         property_graph["graph"]["edges"].append(edge)

   # Save the property graph in JSON format
   if debug:
     print("generated property graph:")
     print(property_graph)
   with open(out_file, "w") as output_file:
     json.dump(property_graph, output_file, indent=4)

   return
    
