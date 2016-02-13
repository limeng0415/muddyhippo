fn="t.txt"

cmd={}
meta={}
for line in open(fn).readlines():
	if line.strip() == "":
		continue
	name = line.split(":")[0].strip()
	body = ""
	note = ""
	if "//" in line:
		body = line.split("//")[0].strip()
		if "^_^" in line.split("//")[1].strip():
			note = line.split("//")[1].split("^_^")[1].strip()
		else:
			note = ""
	else:
		body = line.strip()
	cmd[name] = body
	meta[name] = [n.strip() for n in note.split(",")]
#print cmd
print meta



