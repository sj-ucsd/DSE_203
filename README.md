# DSE_203
203 project
## Package details
**sstopgraph** package takes a semistructured data in json format as input and generates pgraph in json format as output. 
The package is available from test Pypi at https://test.pypi.org/project/sstopgraph-pkg/1.1/ 
### build instructions 
To build and deploy the package locally, recommend following steps:
1. Create a virtual environment. Example steps to create and activate virutal environment are as follows:
   - Change to your working directory
   - python3 -m venv <name of your virtual environment>. For example `python -m venv dse203` will create a virtual environment named dse203
   - Activate virtual environment. On Linux/Mac, run `source myenv/bin/activate` on Windows, `myenv/bin/activate`
   - **Note:** virtual environment can also be created using `conda` and in such case the following steps \
     still apply and allow one to import **sstopgraph** in jupyter notebook. This step has not been tested. 
2. download the **sstopgraph_pkg**. Perform following steps:
   - To install the pacakge in the virtual environment above, after actvation, run `pip install -e .` This step will build the **sstopgraph** package locally and available to be imported in any python program
   - to check correct installation, run python on terminal and type `from sstopgraph import sstopgraph` - this should work correctly
### Usage
1. To check usage, see the example file **test_sstopgraph_transform.py**
2. Sample code once installed:
   ```
   from sstopgraph import sstopgraph
   sstopgraph.semistruct_to_pgraph(<input file name including path>, \
         <mapping configuration file name including path>,[output file name including path],[debug=True])
   ```
   If output file is not specified, an output file with name pgraph.json is automatically generated. debug parameter is optional. 
   
### Input File
1. Input File needs to be a well formed json file.
2. The initial version of this translator will only recognize nodes that are  one level below the root of teh JSON file (i.e. no nested data that will become nodes)
3. Template of a data input file is as follows:
   {
      "node" :[
      {
         "attribute1":"value1",
         "attribute2":"value2",
         ...
      },
      {
         ...
      },
      ...],
   "some other kind of node" :[
         {
         "attribute1":"value1",
         "attribute2":["value2a","value2b","value2c","value2d"],
         ...
      },
      {
         ...
      },
      ...],
   ...
}
4. See examples in the input_files folder: people.json, movies.json, and books.json

### Mapping Configuration File
Mapping Configuration Files are used to provide the instructions on which fileds in the data input file apply to which elemnts in a property graph. 

1. In this initial version of the translator, the mapping configuration file will generate nodes and edges with some fixed fields for each node (id, label, node_type, node-properties) and edge (id, relationship, direction, _source, _target, edge-properties). If the data file does not have input that goes into one of these fields, then the field is still included but the value would be an empty string "".
2. Networkx is used to generate the graph internally to the translator, so the id is used as the displayed value for the node.
3. Template Mapping Cofiguration File looks like the following:
{
    "schema-map": {
        "nodes": [
            {
                "node-type": "jsonpath", (ex: "$.People") This is the root path. 
                "label": "type of node", (ex: "People")
                "node-id": "jsonpath",	(ex: "$.People.id")
                "node-properties": {
                    "key": "jsonpath",
                    "key": "jsonpath",
                    ...
                }
            }
        ],
        "edges": [
            {
                "edge-type": "jsonpath",	(ex: "$.People") This is the root path. 
                "relationship": "value",	(ex: "Is_Friends_with")
                "direction": "Out",			(possible values: "In", "Out", "Both", "None")
                "edge-id": "value",			(ex: "1") If this value is an empty string, then the translator will generate an id.
                "edge-properties": "",		(In this case the edge doesn't have any properties to add, but it could if you added them in like shown in the node properties above.)
                "_source": "jsonpath",	(ex: "$.People.id") This is the location of the data that is the source point of the edge node connection.
                "_target": "jsonpath"	(ex: "$.People.friends") This is the location of the data that is the target point of the edge node connection.
            }
        ]
    }
}
      {
         ...
      },
      ...],
   ...
}
4. See examples in the input_files folder: people_map_cfg.json, movies_map_cfg.json, and books_map_cfg.json
