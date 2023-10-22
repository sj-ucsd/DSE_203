# DSE_203
203 project
## Package details
**sstopgraph** package takes a semistructured data in json format as input and generates pgraph in json format as output. 
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
3. To check usage, see the example file **test_sstopgraph_transform.py** 
