-- dbt_tickets/macros/cast_timestamp.sql
-- Este arquivo é uma macro do dbt que realiza a conversão de valores para o tipo timestamp.
-- A macro permite que os usuários façam casts de diferentes tipos de dados para timestamp de forma eficiente,
-- facilitando a manipulação e análise de dados em modelos de dados no dbt.

{% macro cast_timestamp(expression) %}
    ({{ expression }})::timestamp
{% endmacro %}
