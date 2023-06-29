def CDO_griddes(filename):
  # gets information about grid of NetCDF file using CDO griddes operator
  # results are stored in dictionary
  # written by Klemens Barfus, June, 27th, 2023 

  import subprocess
  sys_cmd = ["cdo griddes "+filename]
  output = subprocess.check_output(sys_cmd, shell=True)
  output = output.decode("utf-8")
  output = output.split("\n")
  n_output = len(output)
  res = {}
  for ii in range(3, n_output-1):
    temp = output[ii].strip()
    temp2 = temp.split("=")
    key = temp2[0].strip()
    if(key in ["gridsize", "xsize", "ysize"]):
      value = int(temp2[1])
    else:
      if(key in ["xfirst", "xinc", "yfirst", "yinc"]):
        value = float(temp2[1])
      else:
        value = temp2[1].strip()
    res[key] = value
  return res





  
