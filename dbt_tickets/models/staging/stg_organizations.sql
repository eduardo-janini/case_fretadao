{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_organizations') }}
),

tipagem as (
    select
        -- IDs 
        {{ cast_int("payload ->> 'id'") }} as organization_id,
        payload ->> 'external_id' as external_id,

        -- Dates
        {{ cast_timestamp("payload ->> 'created_at'") }} as created_at,
        {{ cast_timestamp("payload ->> 'updated_at'") }} as updated_at,
        
        -- Strings
        payload ->> 'name' as name
    from
        source
)

select * from tipagem