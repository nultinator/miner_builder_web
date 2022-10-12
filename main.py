###Get miner type
print("Do you use miniZ or Gminer?")
miner = input()

### Get mining pool url
print("please enter mining pool url\nexample: ycash.dapool.io:3344")
pool_url = input()

### Get mining address
print("please enter a ycash address\nexample: s1QZvkYSqZWGQwTpw3Zbe9VmScoinsDD5LM\nor: ys1enumq74mkcv22werl905h56qcmmqum9dztu2gwsr73tv75g20s5xdful800hd2n4gh9vuee9yvm")
ycash_address = input()

### print information to the console
if miner.lower() == "gminer":
  miner_info = "./miner --algo 192_7 --pers ZcashPOW --server " + pool_url + " --user " + ycash_address
elif miner.lower() == "miniz":
  miner_info = "./miniZ --url=" + ycash_address + "@" + pool_url + " --par=192,7 --pers ZcashPOW -p x"
else:
  print("Something went wrong")
print("Please copy/paste the text below into your mine_ycash file\n")
print(miner_info)
print("\n\n NOTE: If you are on Windows, save with the file extension '.bat', if you are on Linux, please save with the file extension '.sh'")