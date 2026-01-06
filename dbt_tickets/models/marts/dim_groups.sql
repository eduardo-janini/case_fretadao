{{ config(
    materialized='table',
    unique_key='group_id',
    tags=['dim']
) }}

select
    group_id,
    created_at,
    updated_at,
    group_name,
    group_description
from
    {{ ref('stg_groups') }}