{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_groups') }}
),

tipagem as (
    select
        -- IDs 
        (payload ->> 'id')::int as group_id,

        -- Dates
        (payload ->> 'created_at')::timestamp as created_at,
        (payload ->> 'updated_at')::timestamp as updated_at,

        -- Strings
        payload ->> 'name' as name,
        payload ->> 'description' as description,
        
    from
        source
)

select * from tipagem