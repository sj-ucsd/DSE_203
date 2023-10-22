import sys
import getopt
from sstopgraph import sstopgraph

def process_cmdline(argv):
   file_list = dict() 
   debug = False
   try:
     opts, args = getopt.getopt(argv, "hi:m:o:d")
   except getopt.GetoptError:
        print("Usage:test_sstopgraph_transform  -i <input_file> -m map config file -o <output_file> -v")
        sys.exit(2)
   for opt, arg in opts:
     if opt == "-h":
       print("Usage:test_sstopgraph_transform  -i <input_file> -m map config file -o <output_file> -v")
       sys.exit()
     elif opt == "-i":
       file_list['in_file']=arg
     elif opt == "-m":
       file_list['map_cfg_file']=arg
     elif opt == "-o":
       file_list['out_file']=arg
     elif opt == "-d":
       debug = True
     else:
       print("Error! invalid option")
     # error check
   flist_keys = file_list.keys()
   if 'in_file' not in flist_keys or 'map_cfg_file' not in flist_keys:
     print("Error! Input file and Mapping Configuration file are mandatory")
     sys.exit(2)
   if 'out_file' not in flist_keys: # default if output not specified
     file_list['out_file'] = './pgraph.json'

   return file_list,debug

if __name__ == "__main__":
   args = sys.argv[1:] # commandline arguments
   # get input files
   flist,debug = process_cmdline(args)
   # perform transform
   print (flist)
   sstopgraph.semistruct_to_pgraph(flist['in_file'], \
                                     flist['map_cfg_file'],\
                                     flist['out_file'],debug=debug)

  
