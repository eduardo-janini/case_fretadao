{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_users') }}
),

tipagem as (
    select
        -- IDs 
        {{ cast_int("payload ->> 'id'") }} as user_id,
        {{ cast_int("payload ->> 'organization_id'") }} as organization_id,
        payload ->> 'external_id' as external_id,

        -- Dates
        {{ cast_timestamp("payload ->> 'created_at'") }} as created_at,
        {{ cast_timestamp("payload ->> 'updated_at'") }} as updated_at,

        -- Strings
        payload ->> 'name' as name,
        payload ->> 'email' as email,

        -- Booleans
        {{ cast_boolean("payload ->> 'active'") }} as active
    from
        source
)

select *
from(
{{ dedup(
    relation = 'tipagem',
    partition_by = ['user_id'],
    order_by = ['updated_at', 'created_at']
) }}
) as final