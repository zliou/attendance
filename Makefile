t:
	@git status

st: 
	@ls
	@git status

cst:
	@clear
	@pwd
	@echo
	@ls
	@echo
	@git status

test:
	@python attendance.py names.tsv
