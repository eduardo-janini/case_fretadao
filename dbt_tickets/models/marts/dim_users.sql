{{ config(
    materialized='table',
    unique_key='user_id',
    tags=['dim']
) }}

select
    *
from
    {{ ref('stg_users') }}