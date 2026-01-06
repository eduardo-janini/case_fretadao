{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_groups') }}
),

tipagem as (
    select
        -- IDs 
        {{ cast_int("payload ->> 'id'") }} as group_id,

        -- Dates
        {{ cast_timestamp("payload ->> 'created_at'") }} as created_at,
        {{ cast_timestamp("payload ->> 'updated_at'") }} as updated_at,

        -- Strings
        payload ->> 'name' as group_name,
        payload ->> 'description' as group_description
    from
        source
)

select *
from(
{{ dedup(
    relation = 'tipagem',
    partition_by = ['group_id'],
    order_by = ['updated_at', 'created_at']
) }}
) as final