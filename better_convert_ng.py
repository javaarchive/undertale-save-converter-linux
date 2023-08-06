import json, os
print("ensure saves files are in the dir")
print("currently supporting conversion to sav format")
sources = ["file0", "file8", "file9", "undertale.ini"]

with open("undertale.sav.converted", "w") as f:
    kv = {"default":""}
    for filename in sources:
        if os.path.isfile(filename):
            print("Adding",filename)
            with open(filename, "r") as f2:
                kv[filename] = f2.read()
    json.dump(kv, f)
    f.write("\x00")
