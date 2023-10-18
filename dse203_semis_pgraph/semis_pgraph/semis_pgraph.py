import sys, getopt

def parse_arg(argv):
   in_file = ""
   map_cfg_file = ""
   out_file = ""
   opts, args = getopt.getopt(argv,"hi:m:o:")
   for opt, arg in opts:
     if opt == '-h': # help
        print("-h help \n \
               -i input file - mandatory \n \
               -m mapping configuration file - mandatory \n \
               -o output file optional \n")
     elif opt == '-i':
        in_file = arg
     elif opt == '-m':
        map_cfg_file = arg
     elif opt == '-o':
        out_file = arg
   if in_file == "" or map_cfg_file == "":
     print("Error! Missing mandatory parameters: input file and mapping configuration file\n")
     sys.exit(2)
   if out_file == "":
     out_file = './property_graph.json' 

   file_dict = {'in_file':in_file,'map_cfg_file':map_cfg_file, \
                   'out_file':out_file}
   return file_dict

def semis_pgraph(argv):
   file_dict = parse_arg(argv)
   print(file_dict)

if __name__ == "__main__":
   args = sys.argv[1:]
   semis_pgraph(args)
