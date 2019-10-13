fileOut = open("logStash.conf", 'w')
fileOut.writelines("input {\n")

with open("rssLinks.txt", "r") as fileIn:
    for line in fileIn:
        if "http" in line:
            fileOut.writelines("\n".join(('	rss {', '		interval => 3600', '		url => "' + line[:-1] + '"', '	}\n')))

fileOut.writelines("}\n")

with open("Template.conf", "r") as fileIn:
    fileOut.writelines(fileIn.readlines())
fileOut.close()
