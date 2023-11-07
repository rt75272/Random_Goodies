python = python3
MV = mv

all:
	@$(python) GetData.py

# organized:
# 	mv !(GetData.py|Makefile|queries.txt|dumpfiles) dumpfiles

auto:
	@$(python) GetData.py -auto

fire: auto organized

clean:
	clear