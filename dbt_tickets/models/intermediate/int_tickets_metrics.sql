with reference as (

    select
        ticket_id,
        custom_fields
    from {{ ref('stg_tickets') }}

),

exploded as (

    select
        ticket_id,
        (field ->> 'id')::int     as field_id,
        field ->> 'value'         as field_value
    from reference
    cross join lateral jsonb_array_elements(custom_fields) as field
),

filtro as (

    select *
    from exploded
    where field_id between 1 and 5

),

pivotagem as (

    select
        ticket_id,

        max(case when field_id = 1 then field_value end) as tipo_servico,
        max(case when field_id = 2 then field_value end) as desc_regiao,
        max(case when field_id = 3 then field_value end) as tipo_contrato,
        max(case when field_id = 4 then field_value end) as tipo_veiculo,
        max(case when field_id = 5 then field_value end) as tipo_fretamento

    from filtro
    group by ticket_id

)

select 
    ticket_id,
    assignee_id,
    group_id,
    organization_id,
    created_at,
    updated_at,
    channel,
    status,
    priority,
    type as ticket_type,
    description,
    url,
    public,
    tipo_servico,
    desc_regiao,
    tipo_contrato,
    tipo_veiculo,
    tipo_fretamento
from {{ ref('stg_tickets') }} as stg
    left join pivotagem as piv using(ticket_id)