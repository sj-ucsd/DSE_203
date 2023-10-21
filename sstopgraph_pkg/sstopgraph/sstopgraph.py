import json
def semistruct_to_pgraph(in_file, mapcfg_file, out_file='./pgraph.txt',debug=False):
   # check for input errors
   if not in_file:
     print('Error! input file missing')
     sys.exit(2)
   elif not mapcfg_file:
     print('Error! mapping configuration file missing')
     sys.exit(2)
   if debug:
     print('input file = {}, mapping configuration file = {}, output file = {}'.format(in_file, mapcfg_file, out_file))

   # read file input file containing json format semi-structured data 
   # and mapping configuraton file in json format
   try:
      with open(in_file,'r') as input_json:
        semi_struct = json.load(input_json)
      if debug:
        print(semi_struct)
   except Exception as e:
      print("Input file Error! {}".format(e) )
   
   try:
      with open(mapcfg_file, "r") as mapping_file:
        mapping_config = json.load(mapping_file)
      if debug:
        print(mapping_config)
   except Exception as e:
      print("Mapping configuration file Error! {}".format(e) )
   
   # Initialize the property graph
   property_graph = {
     "graph": {
        "nodes": [],
        "edges": []
     }
   }

   # Save the property graph in JSON format
   with open("property_graph.json", "w") as output_file:
     json.dump(property_graph, output_file, indent=4)

   return
    
