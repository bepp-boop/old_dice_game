#!/usr/bin/env make

# Change this to be your variant of the python command
#PYTHON = python3
#PYTHON = python
PYTHON = py


install:
	$(PYTHON) -m pip install -r requirements.txt

unittest:
	 $(PYTHON) -m unittest discover . "*_test.py"

coverage:
	$(PYTHON) -m unittest discover . "*_test.py"
	coverage html
	coverage report -m

pylint:
	pylint Gamefile

flake8:
	flake8

#For Window terminal without bash
pydoc:
	$(PYTHON) -m pydoc -w Cage_test Dice_test EasyCom_test Game_test HardCom_test HumanPlayer_test Player_test Gamefile.Cage Gamefile.Dice Gamefile.EasyCom Gamefile.Game Gamefile.HardCom Gamefile.HumanPlayer Gamefile.main Gamefile.Player
	move *.html document

uml:
	@echo graphviz need to be download outside of the vertul enviroment before running uml
	@echo Install 'choco install graphviz' as admin in none venv for Window
	pyreverse -o png .\Gamefile
	move *.png document\uml

radon-cc:
	radon cc . -a

radon-mi:
	radon mi .

radon-raw:
	radon raw .

radon-hal:
	radon hal .

bandit:
	bandit -r .

lint: flake8 pylint

test: lint coverage
