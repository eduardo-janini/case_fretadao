{{ config(
    materialized='table',
    unique_key='organization_id',
    tags=['dim']
) }}

select
    organization_id,
    external_id,
    created_at,
    updated_at,
    organization_name
from
    {{ ref('stg_organizations') }}