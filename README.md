# Case Analytics Engineer III

## Arquitetura
API → RAW → STAGING → INTERMEDIATE → MARTS → ANALYSES

## Key Decisions
- Ingestão incremental usando `start_time` da API
- Atualização completa para entidades tipo dimensão
- Camada raw apenas para anexação com deduplicação em staging
- Tipagem rigorosa e macros dbt reutilizáveis
- Modelos intermediários apenas para dados aninhados ou baseados em eventos

## Como rodar
docker compose up
python -m raw_layer.run_all
dbt run
dbt test
dbt docs serve