{{ config(materialized='view') }}

with tratamento as (
    select
    t.ticket_id,
    t.tipo_servico,
    tm.solved_at - tm.created_at as tempo_solucao
from
    {{ ref("fat_tickets")}} as t
    inner join {{ ref("fat_ticket_metrics") }} as tm using(ticket_id)
where
    tm.solved_at is not null)
select
    tipo_servico,
    avg(tempo_solucao) as tempo_medio_solucao
from
    tratamento
group by
    tipo_servico
order by
    tempo_medio_solucao desc