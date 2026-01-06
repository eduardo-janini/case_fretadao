-- dbt_tickets/macros/cast_boolean.sql
-- Este arquivo é uma macro do dbt que realiza a conversão de valores para o tipo booleano.
-- A macro permite que os usuários façam casts de diferentes tipos de dados para booleano de forma eficiente,
-- facilitando a manipulação e análise de dados em modelos de dados no dbt.

{% macro cast_boolean(expression) %}
    ({{ expression }})::boolean
{% endmacro %}
