{{ config(materialized='view') }}


with reference as (
    select
        ticket_id,
        custom_fields
    from 
        {{ ref('stg_tickets') }}
),

exploded as (
    select
        ticket_id,
        (field ->> 'id')::int as field_id,
        field ->> 'value'     as field_value
    from
        reference
        cross join lateral jsonb_array_elements(custom_fields) as field
),

filtro as (
    select
        *
    from 
        exploded
    where
        field_id between 1 and 5
),

pivot as (
    select
        ticket_id,

        max(case when field_id = 1 then field_value end) as tipo_servico,
        max(case when field_id = 2 then field_value end) as desc_regiao,
        max(case when field_id = 3 then field_value end) as tipo_contrato,
        max(case when field_id = 4 then field_value end) as tipo_veiculo,
        max(case when field_id = 5 then field_value end) as tipo_fretamento
    from
        filtro
    group by
        ticket_id
)

select
    stg.ticket_id,
    stg.assignee_id,
    stg.group_id,
    stg.organization_id,
    stg.created_at,
    stg.updated_at,
    stg.channel,
    stg.status,
    stg.priority,
    stg.type as ticket_type,
    stg.description,
    stg.url,
    stg.public,

    piv.tipo_servico,
    piv.desc_regiao,
    piv.tipo_contrato,
    piv.tipo_veiculo,
    piv.tipo_fretamento
from 
    {{ ref('stg_tickets') }} as stg
    left join pivot as piv using(ticket_id)