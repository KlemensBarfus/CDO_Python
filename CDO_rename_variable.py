# renames variables applying CDO
# when using an * as comand line argument, you may need to prevent the shell from 
# interpretation by using "\" before, e.g:
# python -u CDO_rename_variable.py /scratch/ws/0/barfus-DCUA/StatModel/ERA5_BLH_\*.nc var159 BLH 
# IMPORTANT: only works for NetCDF files since renaming of variables is not intended for GRIB files

import sys
import glob

def CDO_rename_variable(search_pattern, name_to_replace, new_name):
  import glob
  import os
  from find_temporary_filename import find_temporary_filename
  
  files = glob.glob(search_pattern)
  for ff in files:
    temporary_filename = find_temporary_filename(ff)
    sys_cmd = "cdo -chname,"+name_to_replace.strip()+","+new_name+" "+ff+" "+temporary_filename
    print(sys_cmd)
    os.system(sys_cmd)
    sys_cmd = "mv "+temporary_filename+" "+ff
    os.system(sys_cmd)

def main():
  import sys
  search_pattern = sys.argv[1]
  name_to_replace = sys.argv[2]
  new_name = sys.argv[3]
  CDO_rename_variable(search_pattern, name_to_replace, new_name)

if __name__ == "__main__":
    main()








