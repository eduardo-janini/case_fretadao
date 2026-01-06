{{ config(
    materialized='table',
    unique_key='organization_id',
    tags=['dim']
) }}

select
    *
from
    {{ ref('stg_organizations') }}