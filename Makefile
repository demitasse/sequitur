default:	build

PYTHON	= python

build:
	$(PYTHON) setup.py build
build-py:
	$(PYTHON) setup.py build_py

.PHONY:	build

test:	build
	mkdir -p tmp-test-install
	$(PYTHON) setup.py install --skip-build --prefix tmp-test-install
	export PYTHONPATH=tmp-test-install/lib/python2.7/site-packages; \
	$(PYTHON) test_mGramCounts.py		;\
#	$(PYTHON) test_SparseVector.py		;\
#	$(PYTHON) test_LanguageModel.py		;\
	$(PYTHON) test_Minimization.py		;\
	$(PYTHON) test_SequenceModel.py		;\
#	$(PYTHON) test_IntTuple.py		;\
	$(PYTHON) test_sequitur.py
#	rm -r tmp-test-install

#INSTALL_TARGET = $(HOME)/sr/lib-$(ARX)
INSTALL_TARGET = /u/golik/work/g2p

install: build
	umask 022; \
	$(PYTHON) setup.py install --skip-build --home $(INSTALL_TARGET)

clean:
	rm -rf tmp-test-install
	rm -f *~
	rm -rf build dist
	rm -f *.pyc
	rm -f SparseVector.c
	rm -f sequitur_.py sequitur_wrap.cpp


release:
	d=$$(mktemp -d); \
	  mkdir $$d/g2p; \
	  cp *.cc *.hh *.py *.pyx *.i *.sh CHANGES LICENSE README Makefile $$d/g2p; \
	  cd $$d; \
	  rm g2p/sequitur_.py; \
	  tar cvzf g2p.tar.gz g2p; \
	  rm -rf g2p; \
	  cd -; \
	  mv $$d/g2p.tar.gz .

# ---------------------------------------------------------------------------

TARGETS	= \
	_sequitur_.so sequitur_.py	\
	Evaluation.py  Minimization.py SequenceModel.py sequitur.py g2p.py \
	misc.py tool.py

