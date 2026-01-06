{{ config(materialized='view') }}

with source as (
    select payload from {{ source('raw', 'raw_tickets') }}
),

tipagem as (
    select
        -- IDs 
        {{ cast_int("payload ->> 'id'") }} as ticket_id,
        {{ cast_int("payload ->> 'assignee_id'") }} as assignee_id,
        {{ cast_int("payload ->> 'group_id'") }} as group_id,
        {{ cast_int("payload ->> 'organization_id'") }} as organization_id,

        -- Dates
        {{ cast_timestamp("payload ->> 'created_at'") }} as created_at,
        {{ cast_timestamp("payload ->> 'updated_at'") }} as updated_at,
        
        -- Strings
        payload ->> 'channel' as channel,
        payload ->> 'status' as ticket_status,
        payload ->> 'priority' as priority,
        payload ->> 'type' as ticket_type,
        payload ->> 'description' as ticket_description,
        payload ->> 'url' as ticket_url,

        -- Booleans
        {{ cast_boolean("payload ->> 'public'") }} as public,

        -- Demais campos
        payload -> 'custom_fields' as custom_fields
    from
        source
)

select *
from(
{{ dedup(
    relation = 'tipagem',
    partition_by = ['ticket_id'],
    order_by = ['updated_at', 'created_at']
) }}
) as final