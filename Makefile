# GET ITSG-33 DATA

.PHONY: download-yaml
download-yaml:
		curl -sL 'https://raw.githubusercontent.com/cds-snc/ITSG-33-definitions/master/ITSG-33a.yaml' > data/itsg-33.yaml