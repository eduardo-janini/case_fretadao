-- dbt_tickets/macros/cast_int.sql
-- Este arquivo é uma macro do dbt que realiza a conversão de valores para o tipo inteiro.
-- A macro permite que os usuários façam casts de diferentes tipos de dados para inteiro de forma eficiente,
-- facilitando a manipulação e análise de dados em modelos de dados no dbt.

{% macro cast_int(expression) %}
    ({{ expression }})::int
{% endmacro %}
