{{ config(
    materialized='table',
    unique_key='group_id',
    tags=['dim']
) }}

select
    *
from
    {{ ref('stg_groups') }}