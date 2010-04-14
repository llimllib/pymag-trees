import re
fin = file("article_preview.html")
strip_html = re.compile(r'<(.)*?>')

lines = []
for line in fin:
    if line.startswith("<p"):
        line = strip_html.sub("", line)
        s = line.split(' ')
        lines.append((len(s), line[0:10]))

print "average: ", sum(l[0] for l in lines) / float(len(lines))
