export PYTHON = python3.5

UNIT_TESTS = $(wildcard ./Tests/Unit/**/[^__]*.py ./Tests/Unit/[^__]*.py)
SCRIPT_TESTS = $(wildcard ./Tests/Script/**/[^__]*.sh)

unittests:
	for unit_test in ${UNIT_TESTS} ; do \
		echo "==> Testing $$unit_test" ;\
		$(PYTHON) $$unit_test ;\
	done

scripttests:
	for script_test in ${SCRIPT_TESTS} ; do \
		echo "==> Testing $$script_test" ;\
		./$$script_test ;\
	done

tests: unittests scripttests
