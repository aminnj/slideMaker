
def parseOptions(optString):
    opts = { }
    for optName in listOfOptions:
        opts[optName] = False

    for opt in optString.split("--"):
        opt = opt.strip()
        if(len(opt.split()) < 1): continue
        optName = opt.split()[0].strip()
        if(optName not in listOfOptions): 
            print ">>> Warning: unrecognized option:",optName
            continue

        if(len(opt.split()) < 2):
            opts[optName] = True
        else:
            opts[optName] = " ".join(opt.split()[1:])

    return opts


listOfOptions = ["dump", "title", "caption"]
print parseOptions("--dump --title left --caption this is stupid --unrecognizedopt")
