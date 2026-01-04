{% macro cast_timestamp(expression) %}
    ({{ expression }})::timestamp
{% endmacro %}
