# DSE_203
203 Group 1 Assignment 1
Sagar Jogadhenu, Prakhar Shukla, Laben Fisher
## Package details
**sstopgraph** package takes a semistructured data in json format as input and generates pgraph in json format as output. 
The package is available from test Pypi at https://test.pypi.org/project/sstopgraph-pkg/
### build instructions 
To build and deploy the package locally, recommend following steps:
1. Create a virtual environment. Example steps to create and activate virutal environment are as follows:
   - Change to your working directory
   - python3 -m venv \<name of your virtual environment\>. For example `python -m venv dse203` will create a virtual environment named dse203
   - Activate virtual environment. On Linux/Mac, run `source myenv/bin/activate` on Windows, `\<name of your virtual environment\>/bin/activate`
   - **Note:** virtual environment can also be created using `conda` and in such case the following steps \
     still apply and allow one to import **sstopgraph** in jupyter notebook. This step with conda has not been tested. 
2. download the **sstopgraph_pkg**. Perform following steps:
   - To install the pacakge in the virtual environment above, after actvation, run `pip install -e .` This step will build the **sstopgraph** package locally and available to be imported in any python program within the virtual environment
   - to check correct installation, run python on terminal and type `from sstopgraph import sstopgraph` - this should work without errors
### Usage
1. To check usage, see the example file **test_sstopgraph_transform.py**
  - To run test_sstopgraph_transform.py, use it `python test_sstopgraph_transform.py -i \<input file name\> -m \<mapping config file\> -o [output file] -d [True|False]`
  - Output file is optional and if not specified, will automatically generate pgraph.json
  - -d option for debug. Default debug is False
3. Sample code execution statement from a python file or a Jupyter Notebook:
   ```
   from sstopgraph import sstopgraph
   sstopgraph.semistruct_to_pgraph(<input file name including path>, \
         <mapping configuration file name including path>,[output file name including path],[debug=True])
   ```
4. Specific example of code execution statment from the command line:
   ```
   python test_sstopgraph_transform.py -i ~/DSE_203/input_files/people.json -m ~/DSE_203/input_files/people_map_cfg.json -o people_pgraph.json
   ```
   If output file is not specified, an output file with name pgraph.json is automatically generated. debug parameter is optional. 
   
## Input File
1. Input File needs to be a well formed json file.
2. The initial version of this translator will only recognize nodes that are one level below the root of the JSON file (i.e. no nodes nested inside other nodes from the source data file)
3. Template of a data input file is as follows:
   
```
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

```
4. See examples in the input_files folder: people.json, movies.json, and books.json

## Mapping Configuration File
Mapping Configuration Files are used to provide the instructions on which fileds in the data input file apply to which elements in a property graph. 

1. In this initial version of the translator, the mapping configuration file will generate nodes and edges with some fixed fields for each node (id, label, node_type, node-properties) and edge (id, relationship,  _source, _source_type, _target, _target_type). The node.node-properties consists of the following pattern: "attribute" {"data_type" : "<data_type_name>", "data_value" : "<value>"} (ex: "age": {"data_type":"numeric", "data_value":"22"}). If the data file does not have input that goes into one of these fields, then the field is still included but the value would be an empty string "" .
2. Template Mapping Cofiguration File looks like the following:
```
{
    "schema-map": {
        "nodes": [
            {
                "node-type": "jsonpath", (ex: "$.People") This is the root path. 
                "label": "type of node", (ex: "People")
                "node-id": "attribute",	(An attribute value inside the node-type. For example, if the node had a attribute "name" if the following path was valid in the node $.People.name)
                "node-properties": {
                    "attribute" : {"data_type" : "<data_type_name>", "data_value" : "<value>"},
                    "attribute" : {"data_type" : "<data_type_name>", "data_value" : "<value>"},
                    ...
                }
            }
        ],
        "edges": [
            {
                "edge-type": "jsonpath",	(ex: "$.People") This is the root path. 
                "relationship": "value",	(ex: "Is_Friends_with")
                "edge-id": "value",			(ex: "1") If this value is an empty string, then the translator will generate an id.
                "_source": "attribute",	(ex: "id") This is the location of the data that is the source point of the edge node connection.
                "_source_type" : "label" (ex: People) This is the node label that is being referenced
                "_target": "attribute"	(ex: "name") This is the location of the data that is the target point of the edge node connection.
                "_target_type" : "label" (ex: People) This is the node label that is being referenced
            }
        ]
    }
}
      {
         ...
      },
      ...]
   ...
} 

```

3. See examples in the input_files folder: people_map_cfg.json, movies_map_cfg.json, and books_map_cfg.json

## Known issues/limitations
1. Code doesn't support arbitrary parsing of jsonpath expressions to create nodes and edges. Planned for next revision
2. Does not support special characters in strings. Will add utf support in future version
3. For the edges, the _target has to be a property attribute of a node.

## Note:
The original Notebook is included in the directory for reference and for future use by the authors.

