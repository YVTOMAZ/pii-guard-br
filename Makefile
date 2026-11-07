PYTHON ?= python3
KEYRING_BACKEND ?= keyrings.alt.file.PlaintextKeyring

.PHONY: test
test:
	PYTHON_KEYRING_BACKEND=$(KEYRING_BACKEND) $(PYTHON) tests/test_pii.py
	PYTHON_KEYRING_BACKEND=$(KEYRING_BACKEND) $(PYTHON) tests/test_desktop.py
