# Build/Start Project
`docker compose up --build`

# get 'into' the running project
`docker compose exec app bash`

## run a test
`python -m unittest category.tests.unit.domain.test_entities`
