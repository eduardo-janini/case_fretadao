{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_tickets') }}
),

tipagem as (
    select
        -- IDs 
        (payload ->> 'id')::int as ticket_id,
        (payload ->> 'assignee_id')::int as assignee_id,
        (payload ->> 'group_id')::int as group_id,
        (payload ->> 'organization_id')::int as organization_id,

        -- Dates
        (payload ->> 'created_at')::timestamp as created_at,
        (payload ->> 'updated_at')::timestamp as updated_at,
        
        -- Strings
        payload ->> 'channel' as channel,
        payload ->> 'status' as status,
        payload ->> 'priority' as priority,
        payload ->> 'type' as type,
        payload ->> 'description' as description,
        payload ->> 'url' as url,

        -- Booleans
        (payload ->> 'public')::boolean as public,

        -- Demais campos
        payload -> 'custom_fields' as custom_fields
    from
        source
)

select * from tipagem