import sys

footer = "</conference>"
header = sys.stdin.readline()
header += sys.stdin.readline()
is_header = True

for line in sys.stdin:
    
    if line.strip() == footer:
        break

    if is_header:
        f = open("%s.xml" % line.split('"')[3], 'w')
        f.write(header)
        is_header = False
        
    f.write(line)
    
    if line.strip() == "</paper>":
        f.write(footer)
        f.close()
        is_header = True
