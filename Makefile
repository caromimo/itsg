include database.env
export

# MIGRATIONS

.PHONY: migrate-up
migrate-up: 
		@migrate -database postgres://itsg:$(POSTGRES_PASSWORD)@localhost:5432/itsg?sslmode=disable -path migrations up

.PHONY: migrate-down
migrate-down: 
		@migrate -database postgres://itsg:$(POSTGRES_PASSWORD)@localhost:5432/itsg?sslmode=disable -path migrations down

.PHONY: migration
migration:
		migrate create -ext sql -dir migrations -seq $(name)

# GET ITSG-33 DATA

.PHONY: download-yaml
download-yaml:
		curl -sL 'https://raw.githubusercontent.com/cds-snc/ITSG-33-definitions/master/ITSG-33a.yaml' > data/itsg-33.yaml