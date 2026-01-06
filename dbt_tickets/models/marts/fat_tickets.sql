{{ config(
    materialized='table',
    unique_key='ticket_id',
    tags=['fact']
) }}

select
    ticket_id,
    assignee_id,
    group_id,
    organization_id,
    created_at,
    updated_at,
    channel,
    ticket_status,
    priority,
    ticket_type,
    ticket_description,
    ticket_url,
    public,
    tipo_servico,
    desc_regiao,
    tipo_contrato,
    tipo_veiculo,
    tipo_fretamento
from
    {{ ref('int_tickets') }}