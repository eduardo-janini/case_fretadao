{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_users') }}
),

tipagem as (
    select
        -- IDs 
        (payload ->> 'id')::int as user_id,
        (payload ->> 'organization_id')::int as organization_id,
        payload ->> 'external_id' as external_id,

        -- Dates
        (payload ->> 'created_at')::timestamp as created_at,
        (payload ->> 'updated_at')::timestamp as updated_at,
        
        -- Strings
        payload ->> 'name' as name,
        payload ->> 'email' as email,

        -- Booleans
        (payload ->> 'active')::boolean as active
    from
        source
)

select * from tipagem