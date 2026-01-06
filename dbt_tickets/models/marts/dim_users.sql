{{ config(
    materialized='table',
    unique_key='user_id',
    tags=['dim']
) }}

select
    user_id,
    organization_id,
    external_id,
    created_at,
    updated_at,
    user_name,
    email,
    active
from
    {{ ref('stg_users') }}