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
3. Example:
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
      ...]
   
